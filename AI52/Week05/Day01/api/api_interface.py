#import the model provider
import model.model_provider as mp

def API_INTERFACE(request, MODEL_IN_USE):
    mp.MODEL_PROVIDER(request, MODEL_IN_USE)