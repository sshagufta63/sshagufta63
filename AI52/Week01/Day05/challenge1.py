# ⭐ Challenge 1 – Multi-turn Conversation

# Modify your Day 3 program.

# Instead of sending one prompt, send a conversation with at least three messages.

# Example flow:

# User: What is Kubernetes?

# Assistant: ...

# User: Explain it using a restaurant analogy.

# Observe whether the second answer depends on the first.

# Write your observation.
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
    "What is Kubernetes? answer in a single sentence",
    "Explain it using a restaurant analogy, in a single sentence"
]
messageList=[]

for prompt in prompts:
    print(prompt ,": ")
    messagePayload = {'role':'user', 'content': prompt}
    messageList.append(messagePayload)
    response: ChatResponse = chat(model='gemma3:4b', messages=messageList)
    print(response.message.content)
    print(messageList)