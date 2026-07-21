# Challenge 3 – Dictionary

# Represent yourself as a dictionary.

# Example:

# developer = {
#     "name": "...",
#     "experience": 10,
#     "primary_language": "...",
#     "database": "...",
#     "cloud": "...",
#     "learning": "AI"
# }

# Now print:

# Name : Shagufta
# Experience : 10
# ...

# Bonus:

# Print only the keys.


developer = {
    "name": "Shagufta",
    "experience": 10,
    "primary_language": "Java",
    "database": "Oracle",
    "cloud": "GCP",
    "learning": "AI"
}

print("Name: ", developer["name"])
print("Experience: ", developer["experience"])
print("Primary Language: ", developer["primary_language"])
print("Database: " , developer["database"])
print("Cloud: ", developer["cloud"])
print("Learning: ", developer["learning"])

for attr in developer:
    print(attr)
    
