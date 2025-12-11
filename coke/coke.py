amount = 50
accepted_denominations = [5, 10, 25]
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_denominations:
        amount -= coin
    if amount <= 0:
        print(f"Change Owed: {-amount}")
        amount = 0
