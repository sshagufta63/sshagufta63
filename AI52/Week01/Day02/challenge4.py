# Challenge 4 – Functions

# Create

# recommend_model(ram)

# If RAM >= 32

# Return

# Qwen 3 8B

# Else

# Gemma 3 4B

def recommend_model(ram):
    if ram >=32:
        return "Qwen 3 8B"
    else:
        return "Gamma 3 4B"
    
print(recommend_model(int(input())))
