import os
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
print(logo)
print("Welcome to the secret auction program.")
bids = {}
other_bidders = True
winner = ""
highest = 0
while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    check_for_other_bidders = input("Are there any other bidders? Type 'y' for yes, Type 'n' for no. \n")
    if check_for_other_bidders == "n":
        other_bidders = False
    os.system('cls')
for key in bids:
    if bids[key] > highest:
        winner = key
        highest = bids[key]
print(f"The winner is {winner} with a bid of ${bids[winner]}.")
