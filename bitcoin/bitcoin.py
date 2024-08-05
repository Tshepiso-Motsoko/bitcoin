import sys
import requests

def main():
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Get the number of Bitcoins from the command-line argument
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Query the API for the current price of Bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error in fetching Bitcoin price")
    except KeyError:
        sys.exit("Invalid response from API")

    # Calculate the cost of the specified number of Bitcoins
    cost = bitcoins * price

    # Format and output the cost to four decimal places with a thousands separator
    cost_formatted = "{:,.4f}".format(cost)
    print(f"The cost of {bitcoins:,} Bitcoin(s) is ${cost_formatted}")

if __name__ == "__main__":
    main()
