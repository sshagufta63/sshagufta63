#import app provider
#send the request to app provider
#app provider in turn selects the model



MODEL_IN_USE='gemma3:4b'

import Week05.Day01.model.ai_provider as api

print("Ask me something.. ")
input_query = input()

api.API_INTERFACE(input_query, MODEL_IN_USE)

