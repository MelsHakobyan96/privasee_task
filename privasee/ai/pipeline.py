from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
import asyncio
import sys
from .utils import OpenAIChat, VectorDB
from variables import choose_article_prompt_template, modify_request_prompt_template, article_summaries, final_answer_prompt
from config import *


class GDPRQA:
    def __init__(self) -> None:
        choose_article = ChatPromptTemplate.from_template(choose_article_prompt_template)
        modify_request = ChatPromptTemplate.from_template(modify_request_prompt_template)
        final_answer_prompt_template = PromptTemplate(
            input_variables=["request", "relevant_documents", "human_input"],
            template=final_answer_prompt,
        )

        model = OpenAIChat(model=gpt_model, openai_api_key=openai_api_key, temperature=0, timeout=60.0, max_retries=2)
        
        choose_chain = {'request': itemgetter('request')} | choose_article | model | StrOutputParser()
        modify_chain = {'request': itemgetter('request')} | modify_request | model | StrOutputParser()

        self.map_chain = RunnableParallel(choose=choose_chain, modify=modify_chain)

        memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")
        self.final_chain = LLMChain(llm=model, prompt=final_answer_prompt_template, memory=memory)

    async def streaming_print(self, text, delay=0.0001):
        return_response = ""
        for char in text:
            return_response = text
            sys.stdout.write(char)
            sys.stdout.flush()
            await asyncio.sleep(delay)
        sys.stdout.write('\n')

        return return_response

    async def run(self, request):
        map_chain_response = self.map_chain.invoke({"request": request})

        if map_chain_response['choose'] in article_summaries:
            vector_db = VectorDB(collection=map_chain_response['choose'])
        else:
            vector_db = VectorDB(collection="GDPR_Art_1_to_21_full")

        relevant_docs = vector_db.find_relevant_docs(map_chain_response['modify'])
        relevant_docs = '\n-----\n'.join([chunk_content.page_content for chunk_content in relevant_docs])

    
        response = await self.final_chain.ainvoke({"request": request, "relevant_documents": relevant_docs, "human_input": request})
        
        return_response = await self.streaming_print(response["text"], delay=0.0)

        return return_response
