# Get name input from the user
name = input("Enter name: ")
MENU = "(H)ello \n(G)oodbye \n(Q)uit"
print(MENU)
# Get user menu choice
choice = input(">>> ").upper()
while choice != 'Q':
   if choice == 'H':
       print(f"Hello {name}")
   elif choice == 'G':
       print (f"Goodbye {name}")
   else:
       print("Invalid choice")
   print(MENU)
   choice = input(">>> ").upper()
print("Finished.")