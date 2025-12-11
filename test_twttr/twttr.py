def main():
    text = input("Input: ")
    twttr = shorten(text)
    print(f"Twttr: {twttr}")


def shorten(word):
    return "".join([char for char in word if char.lower() not in "aeiou"])

if __name__ == "__main__":
    main()
