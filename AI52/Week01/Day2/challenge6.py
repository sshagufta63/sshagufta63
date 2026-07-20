# Optional Challenge (⭐)

# Since you work with SQL every day...

# Given:

# queries = [
#     "SELECT * FROM customer",
#     "SELECT * FROM employee",
#     "SELECT * FROM orders"
# ]

# Print

# Query 1 has 22 characters.

# Query 2 has ...

# ...

queries = [
     "SELECT * FROM customer",
     "SELECT * FROM employee",
     "SELECT * FROM orders"
 ]
i=0
for query in queries:
    print("Query ", i+=1 ," has ", len(query), "characters")
    #i=i+1