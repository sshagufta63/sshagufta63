# Challenge 2 – Lists

# Create a list of your top five technologies.

# Now print:

# 1. Java
# 2. BigQuery
# 3. SQL
# 4. Kubernetes
# 5. Python

# Bonus:

# Ask the user to enter another technology and append it to the list.


top_five_tech = ["Java", "Bigquery","SQL","Kubernetes","Python"]
print(top_five_tech)

print("Suggest me one to append one to this list : ")
additional = input()
top_five_tech.append( additional)

print(top_five_tech)