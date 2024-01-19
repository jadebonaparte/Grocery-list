#To-Do List
#Jade
#Initialize
GroceryList = ["Apples", "Milk", "Bread", "Eggs", "Yougurt", "Cereal"]

#Functions

def start():
    while True:
        print("Please chose an option to alter your list")
        print(" 1.) Add an item to the list \n 2.) View the current list \n 3.) Mark an item as completed \n 4.) Remove an item from the list \n 5.) Exit the program \n 6.) Remove all items from the list \n 7.) Sort the list alphabetically \n 8.) Count the number of items on the list")
        option = int(input("option: "))
        if option == 1:
            add()
        if option == 2:
            view()
        if option == 3:
            completed()
        if option == 4:
            remove()
        if option == 5:
            exit()
            break
        if option == 6:
            remall()
        if option == 7:
            sort()
        if option == 8:
            count()
            
        
        
#Count the number of items on the To-Do list 
        
def count():
    print(len(GroceryList))

def sort():
    GroceryList.sort(reverse=False)

def remall():
    GroceryList.clear()


def add():
    x = input("What would you like to add to the list?")
    GroceryList.append(x)
    print(GroceryList)

def view():
    print(GroceryList)

def completed():
    ans = input("Select an item from the list to mark as completed: ")
    print(ans)
    i = GroceryList.index(ans)
    print(i)
    GroceryList[i] = ans +  " x"
    print(GroceryList)

def remove():
    print("The items on the list are numbered from left to right starting at zero. Please insert the number of the item you would like to remove.")
    x = int(input("Number: "))
    GroceryList.pop(x)
    print(GroceryList)

def exit():
    print("You have exited the program")


#Main

start()