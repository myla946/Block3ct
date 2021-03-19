"""
programe goals:
3. pull the values stored at specific indexes
4. conver input to INTs
5. put all action in a while loop
6.add exit option
"""
import random
myList = []

def mainProgram():
#build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from following options.  type the number of the choise")
        choise = input("""1. Add to a list,
2. Return a value in a list,
3. Add a bunch
4. random search,
5. Liner search
6. print list
7. quit     """)
        if choise == "1":
            addTolist()
        elif choise == "2":
            indexValues()
        elif choise == "3":
            addAbunch()
        elif choise == "4":
            randomeSearch()
        elif choise == "5":
              linerSearch()
        elif choise == "6":
            print(myList)
        else:
            break
def addToLIst():
    print("Adding to a list! Great choise!")
    newItem = input("Type an interger here!    ")
    myList.append(int(newItem))
    #we need to think about errors!

def addAbunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input(" How many new inegers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?    ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is complete!")
                

def randomSearch():
    print("Why doyou chosie this ")
    print(myList[random.randit(0, len(myList)-1)])

def linerSearch():
    print("WE'er going to go through this list one item at a time!")
    searchValue = input("What are you looking for?    ")
    for x in range(len(myList)):
        if  myList[x] == int(searchValue):
             print("Your item is at index postion  {}".format(x))
        

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index postion here:     ")
    print(myList[int(indexPos)])

if __name__== "__main__":
    mainProgram()



