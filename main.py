from replit import clear
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
print("Welcome to Secret Auction Program")
r=True
dict={}
high=0
while(r):
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    repeat=input("Are there any other bidders? Type 'yes' or 'no'")
    dict[name]=bid
    print(dict)
    clear()
    if(repeat=="no"):
        r=False
        for name in dict:
            val=dict[name]
            if(val>high):
                high=val
                winner=name
        print(f"The winner is {winner} with a bid of ${high}")

