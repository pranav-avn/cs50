while True:
    try:
        x,y = input("Fraction: ").split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        if x<0 or y<0:
            raise ValueError
        percentage = x/y * 100
        if percentage >= 99:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        else:
            print(f"{percentage:.0f}%")
            break
    except (ValueError, ZeroDivisionError):
        continue
