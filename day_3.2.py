import random

r= "Rock"
p= "Paper"
s= "Scissors"
comp = random.randint(0,2)
user = input("Type R for Rock, P for Paper and S for scissors").upper()

print(comp)

if user == "P":
    print(f"You chose {p}")
    print (type(comp))
    if comp == 0:
        print(f"Computer chose {p}, Match Draw!")
    elif comp == 1:
        print(f"Computer chose {r}, Congrats, You won!")
    elif comp == 2:
        print(f"Computer chose {s}, You Lose! \n Please Try Again!")


elif user == "S":
    print(f"You chose {s}")
    if comp == 0:
        print(f"Computer chose {p}, Congrats, You Win!")
    elif comp == 1:
        print(f"Computer chose {r}, You Lose! \n Please Try Again!")
    elif comp == 2:
        print(f"Computer chose {s}, Match Draw!")

elif user == "R":
    print(f"You chose {r}")
    if comp == 0:
        print(f"Computer chose {p}, Congrats, You Win!")
    elif comp == 1:
        print(f"Computer chose {r}, Match Draw!")
    elif comp == 2:
        print(f"Computer chose {s}, You Lose! \n Please Try Again!")
