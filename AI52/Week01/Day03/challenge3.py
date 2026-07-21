# Challenge 1 ⭐

# Your mission:

# Write a Python program that:

# Connects to your local Ollama.
# Uses the Gemma model (or whichever model you downloaded).
# Sends this prompt:
# Explain Kubernetes in one sentence.
# Prints the response.


from ollama import chat
from ollama import ChatResponse



prompts = [
    "what is 1+1, only answer needed",
    "what is 1+2, only answer needed",
    "what is 1+4, only answer needed"
]

for prompt in prompts:
    print(prompt ,": ")
    messagePayload = {'role':'user', 'content': prompt}
    response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload])
    print(response.message.content)