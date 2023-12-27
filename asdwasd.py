import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = input("지시를 내려라 : ")

response = openai.Completion.create(
    model="text-davinci-03",
    prompt=prompt,
    temperature=1,
    max_tokens=4000
)
print("==========================")
print(str(response["choices"][0]["text"]).strip())
print("==========================")
