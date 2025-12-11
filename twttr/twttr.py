text = input("Input: ")
twttr = "".join([char for char in text if char.lower() not in "aeiou"])
print(f"Twttr: {twttr}")
