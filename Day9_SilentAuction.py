from Day9_SilentAuctionArt import logo

print(logo)
def find_max_bid(bid_dict):
    max_bid = 0
    max_bidder = ""

    for bidders in bid_dict:
        if bid_dict[bidders] > max_bid:
            max_bid = bid_dict[bidders]
            max_bidder = bidders
    print(f"Max Bidder is {max_bidder} & his bid is $ {max_bid}")
    # print(max(bid_dict, key=bid_dict.get()))


def silent_bid():
    direction = True
    silent_bidders = {}
    while direction:
        name = input("What's your name : ")
        bid = int(input("What's your bid : $ "))
        silent_bidders[name] = bid
        go_ahead = input("Are there any other Bidders, Type 'Yes' or 'No' : ").lower()
        if go_ahead == "yes":
            print("\n" * 100)
            direction = True
        elif go_ahead == "no":
            direction = False
            find_max_bid(silent_bidders)
        else:
            print("Choose correct option")
            break


silent_bid()
