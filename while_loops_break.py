import random
#
while True:
    # print("infinite")
    choice = input("enter i for an insult, or q to quit: ").strip().lower()
    if choice == "i":
        print(
            f"You are a {random.choice(["carnivore", "dumb dumb", "terrible human being", "waste of flesh"])}")
    elif choice == "q":
        break  # this will exit the loop
    else:
        print("That was not a valid option")
print("Thanks for being a good sport")
