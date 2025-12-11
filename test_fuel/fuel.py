def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        print(gauge(percentage))

def convert(fraction):
    try:
        x,y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        if x<0 or y<0:
            raise ValueError
        return x/y * 100

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()
