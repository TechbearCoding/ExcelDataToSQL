from parseData import *

# Create the menu
      
def print_menu(): 
    print(67 * "-")
    print("Author- techbearHUB")
    print()
    print("Excel data to sql queries")
    print()
    print ("1. Create sql table")
    print ("2. Create sql table with insert Into")
    print ("3. About")
    print ("0. Exit")
    print(67 * "-")
  
loop=True      


while loop:        
    print_menu()
    choice = input("Enter your choice [1-3] or [0] to exit: ")
     
    if choice=="1":     
        print ("Creating create table statement...")
        createStatement(0)
    elif choice=="2":
        print ("Creating create table statement with insert into")
        createStatement(1)
    elif choice=="3":
        print ("Created by MaLe from techbear.org")
    elif choice=="0":
        print ("Exiting...")
        loop=False
    else:
        input("Wrong option selection. Enter any key to try again..")