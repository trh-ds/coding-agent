import os
from openai import OpenAI
from dotenv import load_dotenv
import sys

def main():
    
    load_dotenv()
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("API_KEY"),
    )
    if len(sys.argv)<2:
        print("I need a prompt !!")
        sys.exit(1)
        
    prompt = sys.argv[1]
    
    
    
    
    response = client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
            {"role": "user", "content": prompt}
        ],
        

    )

    print(response.choices[0].message.content)

    print("Token usage: ")
    print(f"Sent tokens (prompt): {response.usage.prompt_tokens}")
    print(f"Received tokens (completion): {response.usage.completion_tokens}")
    
main()