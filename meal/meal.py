def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if converted_time is None:
        print("Invalid time format")
    elif 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    try:
        hours, minutes = map(int, time.split(":"))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return hours + minutes / 60
    except ValueError:
        return None

if __name__ == "__main__":
    main()
