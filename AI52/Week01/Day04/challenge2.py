# ⭐⭐ Challenge 2 – Compare Three Prompts

# Ask the same model:

# Prompt 1

# Explain Kubernetes.

# Prompt 2

# Explain Kubernetes like I'm a Java developer.

# Prompt 3

# Explain Kubernetes to help me prepare for an interview.

# Compare:

# Detail
# Tone
# Structure

# Write your findings.


from ollama import chat
from ollama import ChatResponse


prompts = [
    "Explain Kubernetes.",
    "Explain Kubernetes like I'm a Java developer.",
    "Explain Kubernetes to help me prepare for an interview."
]

for prompt in prompts:
    print(prompt ,": ")
    messagePayload = {'role':'user', 'content': prompt}
    response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload])
    print(response.message.content)