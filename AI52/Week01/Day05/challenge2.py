# ⭐⭐ Challenge 2 – Break the Conversation

# Now remove the first user message.

# Send only:

# Explain it using a restaurant analogy.

# Compare the response.

# Questions to answer:

# Was it different?
# Why?

from ollama import chat
from ollama import ChatResponse



prompts = [
    "Explain it using a restaurant analogy, in a single sentence"
]

for prompt in prompts:
    print(prompt ,": ")
    messagePayload = {'role':'user', 'content': prompt}
    response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload])
    print(response.message.content)