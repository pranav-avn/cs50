def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #start with two letters
    if len(s) < 2 or not s[0:2].isalpha():
        return False
    #only letters and numbers
    if not s.isalnum():
        return False
    #length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False
    #numbers at the end
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
            break
    #first number not '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            break
    return True

if __name__ == "__main__":
    main()
