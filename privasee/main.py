from ai.pipeline import GDPRQA
import asyncio
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'privasee'))

import warnings
warnings.filterwarnings("ignore")

async def main():
    qa = GDPRQA()
    while True:
        user_input = input("\n\n\n\n\n\n\nEnter your request, if you want to exit just write 'exit' > ")
        
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break
        
        print("\n\n", "Analyzing...", "\n\n")
        await qa.run(request=user_input)

if __name__ == "__main__":
    asyncio.run(main())