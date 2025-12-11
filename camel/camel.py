camelCase = input("camelCase: ")
snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in camelCase]).lstrip('_')
print("snake_case: ",snake_case)
