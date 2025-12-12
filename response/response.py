from validator_collection import checkers


def is_valid(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


mail = input("What's your email address? ")
print(is_valid(mail))
