import os
from typing import List, Dict
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.chat_models import ChatOpenAI as LangChainChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import chromadb
import uuid
from langchain.docstore.document import Document
from config import *
from variables import article_summaries


class VectorDB:
    def __init__(self, collection: str):
        self.embedding_function = CustomOpenAIEmbeddings(openai_api_key=openai_api_key)
        persistent_client = chromadb.PersistentClient()
        self.collection = persistent_client.get_or_create_collection(name=collection, embedding_function=self.embedding_function)
        self.db = Chroma(
            client=persistent_client,
            collection_name=collection,
            embedding_function=self.embedding_function
        )
        
    def find_relevant_docs(self, query: str, num_of_results: int=None) -> List[Document]:
        if num_of_results:
            results = self.db.similarity_search(query, k=num_of_results)
            return results
        else:
            results = self.db.similarity_search(query)
            return results

    def add_documents(self, documents: List[Document]):
        for document in documents:
            self.collection.add(ids=[str(uuid.uuid1())], metadatas=document.metadata, documents=document.page_content)

    def delete_document(self, metadata: Dict):
        document_ids = self.find_document_by_metadata(metadata=metadata)['ids']
        self.db._collection.delete(ids=document_ids)

    def find_document_by_metadata(self, metadata: Dict):
        return self.db.get(where=metadata)
    
    def join_all_collections(self):
        persistent_client = chromadb.PersistentClient()

        all_collections = persistent_client.list_collections()
        for collection in all_collections:
            collection_name = collection.name
            if collection_name == self.db._collection.name:
                continue

            source_collection = persistent_client.get_collection(name=collection_name, embedding_function=self.embedding_function)
            documents = source_collection.get()
            for document, metadata in zip(documents['documents'], documents['metadatas']):
               self.collection.add(ids=[str(uuid.uuid1())], metadatas=metadata, documents=document)

    
class OpenAIChat(LangChainChatOpenAI):
    def __init__(self, **kwargs):
        if kwargs.get('openai_organization', None) is None and kwargs.get('base_url', None) is None:
            kwargs['openai_organization'] = openai_organization
        if kwargs.get('model', None) is None:
            kwargs['model'] = "gpt-4-turbo"
        if kwargs.get('temperature', None) is None:
            kwargs['temperature'] = 0.
        kwargs['streaming'] = True
        kwargs['callbacks'] = []
        super().__init__(**kwargs)
        

class CustomOpenAIEmbeddings(OpenAIEmbeddings):

    def __init__(self, openai_api_key, *args, **kwargs):
        super().__init__(openai_api_key=openai_api_key, *args, **kwargs)

    def _embed_documents(self, texts):
        embeddings = [
            self.client.create(input=text, model="text-embedding-ada-002").data[0].embedding 
            for text in texts
        ]
        return embeddings
        
    def __call__(self, input):
        return self._embed_documents(input)
    

def semantic_chunking(full_document):
    text_splitter = SemanticChunker(
        CustomOpenAIEmbeddings(openai_api_key=openai_api_key), breakpoint_threshold_type="percentile",  # "percentile", "standard_deviation", "interquartile"
        # breakpoint_threshold_amount=99
    )
    documents = text_splitter.create_documents([full_document])

    return documents

def create_vector_databases(articles_dir_path: str):
    for filename in os.listdir(articles_dir_path):
        if filename.endswith(".txt"):
            txt_path = os.path.join(articles_dir_path, filename)
            article_number = filename.replace('.txt', '')
            
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            vector_db = VectorDB(collection=article_number)
            documents = semantic_chunking(text)
            for i, document in enumerate(documents):
                document.metadata = {'chunk_number': i, 'article_number': article_number, 'article_summary': article_summaries[article_number]}
            vector_db.add_documents(documents)
            
            print(f"Processed {filename} and added {len(documents)} documents to Collection {vector_db.collection.name}")

if __name__ == "__main__":
    create_vector_databases(r'privasee\GDPR_Art_1_to_21_split\text')
    vdb = VectorDB(collection='GDPR_Art_1_to_21_full')
    vdb.join_all_collections()