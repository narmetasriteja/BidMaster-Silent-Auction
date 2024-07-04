# Define a dictionary to store bids
bids = {}

# Function to add a new bid
def add_bid(name, amount):
    bids[name] = amount

# Function to find the highest bid
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner, highest_bid

# Function to start the auction
def start_auction():
    while True:
        name = input("Enter your name: ")
        amount = float(input("Enter your bid amount: $"))

        add_bid(name, amount)
        
        more_bids = input("Are there any other bids? Type 'yes' or 'no': ").lower()
        if more_bids == 'no':
            break

    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

# Run the auction
start_auction()
