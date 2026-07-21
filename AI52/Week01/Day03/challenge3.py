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

query = "Explain Kubernetes in one sentence."
messagePayload = {'role':'user', 'content':query}

response: ChatResponse = chat(model='gemma4:12b', messages=[messagePayload])


print(response)