from openai import OpenAI

client = OpenAI(api_key="")

prompt = ""

while True:
    prompt = input("you:")
    chat_completion = client.chat.completions.create(
        messages = [
            {
            "role" : "user",
            "content" : prompt
            }
        ],
        model="gpt-3.5-turbo"
    )

    #pront the response
    response_message = chat_completion.choices[0].message.content
    print("AI:",response_message)