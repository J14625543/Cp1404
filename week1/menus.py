MENU = "(H)ello  (G)oodbye  (Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ")

while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid message")
    print(MENU)
    choice = input(">>> ")

print("finished message")
