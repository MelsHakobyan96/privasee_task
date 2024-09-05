from ai.pipeline import GDPRQA
import asyncio
import os
import sys
from feedbackIntelligence.fi import FeedbackIntelligenceSDK
from config_ import fi_api_key
from feedbackIntelligence.schemas import Message, Context, Feedback
import random
sys.path.append(os.path.join(os.path.dirname(__file__), 'privasee'))

import warnings
warnings.filterwarnings("ignore")
sdk = FeedbackIntelligenceSDK(api_key=fi_api_key)

async def main():
    messages = []
    qa = GDPRQA()
    while True:
        user_input = input("\n\n\n\n\n\n\nEnter your request, if you want to exit just write 'exit' > ")
        
        if user_input.lower() == 'exit':
            if messages:
                fi_response = sdk.add_chat( project_id=9, chat_id=random.randint(1, 10000), messages=messages)
                print(fi_response)
            print("Exiting the loop.")
            break
        
        print("\n\n", "Analyzing...", "\n\n")
        full_response = await qa.run(request=user_input)
        messages.extend([
            Message(role='human', text=user_input, propmt='test', 
                    context=Context(text='new_context')),
            Message(role='ai', text=full_response), 
        ])
        


if __name__ == "__main__":
    asyncio.run(main())