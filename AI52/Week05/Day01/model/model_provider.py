from ollama import chat
from ollama import ChatResponse

def MODEL_PROVIDER(prompt, MODEL_IN_USE):    
    prompts =[]
    try:
        #for prompt in prompts:
        # print(prompt ,": ")
            messagePayload = {'role':'user', 'content': prompt}
            response: ChatResponse = chat(model=MODEL_IN_USE, messages=[messagePayload])
            print(response.message.content)
    except:
        print("Unable to get a response from the AI model.\nPlease try again.")