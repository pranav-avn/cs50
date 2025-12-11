def convert(text:str):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input()
    print(convert(text))

if __name__ == "__main__":
    main()
