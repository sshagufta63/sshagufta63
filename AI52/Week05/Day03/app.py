
from ollama import chat
from ollama import ChatResponse
import json

MODEL_IN_USE='gemma3:4b'
def get_table_schema():
     return {
                "table": table_name,
                "columns": [
                    {"name": "id", "type": "INT64"},
                    {"name": "customer_id", "type": "INT64"},
                    {"name": "order_date", "type": "DATE"},
                    {"name": "amount", "type": "NUMERIC"}
                ],
                "partitioned_by": "order_date",
                "clustered_by": ["customer_id"]
            }






prompts =[]
print("Ask me something.. ")
input_query = input()
prompts.append(input_query)
tools= [
    {
        "type": "function",
        "function": {
            "name": "get_table_schema",
            "description": "Returns the schema of a BigQuery table.",
            "parameters": {
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string"
                    }
                },
                "required": ["table_name"]
            }
        }
    }
]

try:
    for prompt in prompts:
    # print(prompt ,": ")
        messagePayload = {'role':'user', 'content': prompt}
        response: ChatResponse = chat(model=MODEL_IN_USE, messages=[messagePayload], tools = tools)
        print(response.choices[0].message)
        print(response.message.content)
        #

        # 1. LLM requests the tool
        tool_call = response.choices[0].message.tool_calls[0]

# 2. Your Python code executes it
        result = get_table_schema(
        tool_call.function.arguments
        )
        prompts.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
})
except:
    print("Unable to get a response from the AI model.\nPlease try again.")