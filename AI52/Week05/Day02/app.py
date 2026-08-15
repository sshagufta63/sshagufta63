
from ollama import chat
from ollama import ChatResponse

MODEL_IN_USE='gemma3:4b'


prompts =[]
print("Ask me something.. ")
input_query = input()
prompts.append(input_query)


try:
    for prompt in prompts:
    # print(prompt ,": ")
        messagePayload = {'role':'user', 'content': prompt}
        response: ChatResponse = chat(model=MODEL_IN_USE, messages=[messagePayload])
        print(response.message.content)
except:
    print("Unable to get a response from the AI model.\nPlease try again.")