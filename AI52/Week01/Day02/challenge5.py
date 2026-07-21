# Challenge 5 – JSON

# Given

# developer = {
#    ...
# }

# Convert it to JSON and save it to

# developer.json

# Then read it back and print it.


developer = {
    "name": "Shagufta",
    "experience": 10,
    "primary_language": "Java",
    "database": ["Oracle", "Bigquery"],
    "cloud": "GCP",
    "learning": "AI"
}
import json

print(json.dumps(developer , indent=4))