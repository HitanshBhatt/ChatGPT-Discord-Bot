from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature= 1,
        max_tokens= 100
    )

    resp_dict = response.get("choices")

    if resp_dict and (len(resp_dict) > 0):
        prompt_response = resp_dict[0]["text"]

    return prompt_response