logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bid={}


def highest_bidder(bid):
    highest = 0
    winner = ""
    for bidder in bid:
        find = bid[bidder]
        if find > highest:
            highest = find
            winner = bidder
    print(f"the highest bid is {highest} and the winner name is {winner} ")


flag = True
while flag == True:
    name = input("Enter the bidder name : ").upper()
    amount = int(input("Enter the bidding amount in $ :"))
    bid[name] = amount
    choice = input(" Enter YES if any other bidder waiting to bid else type NO to close the bidding session : ").upper()
    if "NO" in choice:
        flag = False
highest_bidder(bid)
