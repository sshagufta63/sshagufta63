# ⭐⭐⭐ Challenge 3 – Design a Prompt

# This one is from your world.

# Design a prompt that asks the model to:

# Review a BigQuery SQL query for:

# readability
# performance
# cost optimization

# The query itself can be simple.

# For example:

# SELECT *
# FROM customer
# WHERE country='India'


from ollama import chat
from ollama import ChatResponse

query = '''Review a BigQuery SQL query for:

 readability
 performance
 cost optimization


 SELECT *
 FROM customer
 WHERE country='India'''
messagePayload = {'role':'user', 'content':query}

response: ChatResponse = chat(model='gemma3:4b', messages=[messagePayload])


print(response.message.content)