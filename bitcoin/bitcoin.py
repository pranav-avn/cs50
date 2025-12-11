import sys
import requests
import json

def main():
    g = get_coin()
    req_coin(g)

def get_coin():
    #print(sys.argv)
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

def req_coin(gcoin):
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7f93b232c03f284495ef8424bb2e332f367854771e08583cfb58242f1034790c")
        bitcoin = float(response.json()['data']['priceUsd'])
        result = bitcoin * float(gcoin)
        print(f"${result:,.4f}")
    except requests.RequestException:
        sys.exit(1)


main()
