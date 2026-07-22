# Challenge 1 – Observe Temperature

# Using Ollama, run the same prompt three times.

# Example:

# Explain Kubernetes in one sentence.

# First, use a low temperature.

# Then, use a higher temperature.

# Observe:

# Did the answers change?
# Which setting produced more variation?

from ollama import chat
from ollama import ChatResponse



prompts = [
    "Explain Kubernetes in one sentence.",
    "Explain Kubernetes in one sentence.",
    "Explain Kubernetes in one sentence."
]
temp = 0.1
for prompt in prompts:
    print(prompt ,": ")
    messagePayload = {'role':'user', 'content': prompt}
    response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload], options={
        "temperature": temp  # Higher = more creative, lower = more deterministic
    })
    temp+=0.3
    print(response.message.content)