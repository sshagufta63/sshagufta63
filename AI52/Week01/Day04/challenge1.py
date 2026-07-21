# Challenge 1 – Improve the Prompt

# Start with this prompt:

# Explain BigQuery.

# Now improve it.

# Your goal is to make the answer more useful for you.

# Try adding:

# your experience
# your background
# expected length
# output format

# Run both prompts.


from ollama import chat
from ollama import ChatResponse

query = "Explain BigQuery."
improvedQuery = "Explain Bigquery. " \
"Context: I am java dev writing to integrate app with Bigquery. " \
"Constarint: within 100 words and consider me as beginner. " \
"Output Format: simple language."
messagePayload = {'role':'user', 'content':improvedQuery}

response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload])


print(response.message.content)