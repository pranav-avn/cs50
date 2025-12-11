months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        month, day, year = map(int, date.split("/"))
        if (int(month) >= 1 and int(month) <=12) and (int(day) >= 1 and int(day) <=31):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")
            month = months.index(old_month) + 1
            if old_day.find(",") == -1:
                raise ValueError
            day = int(old_day.replace(",", ""))
            if (int(month) >= 1 and int(month) <=12) and (int(day) >= 1 and int(day) <=31):
                break
        except:
            print()
            pass

print(f"{year}-{month:02}-{day:02}")
