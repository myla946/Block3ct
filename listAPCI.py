"""
programe goals:
1. Add items to list(ints)
2. Offer the user a choise of actions
3. pull the values stored at specific indexes
4. conver input to INTs
5. put all action in a while loop
6.add exit option
"""
myList = []

def mainProgram():
#build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from following options.  type the number of the choise")
        choise = input("1. Add to a list,  2. Return a value in a list    ")
        if choise == "1":
            addTolist()
        elif choise == "2":
            indexValues
        elif choise == "3":
            break
def addToLIst():
    print("Adding to a list! Great choise!")
    newItem = input("Type an interger here!    ")
    myList.append(int(newItem))
    #we need to think about errors!


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index postion here:      ")
    print(myList[int(indexPos)])

if __name__== "__main__":
    mainProgram()



