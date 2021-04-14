"""
programe goals:
3. pull the values stored at specific indexes
4. conver input to INTs
5. put all action in a while loop
6.add exit option
"""
import random
myList = []
uniqu_list = []

def mainProgram():
#build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from following options.  type the number of the choise")
        choise = input("""1. Add to a list,
2. Return a value in a list,
3. Add a bunch
4. Random search,
5. Liner search
6. Sort list
7. print list
8. recursive binary search
9. Quit """)
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
           sortList(myList)
        elif choise == "7":
            printLists()
        elif choise == "8":
            searchItem = input("What are you looking for?   ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
        else:
            break
def addToList():
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

def sortLists(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unque_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new, sorted list?    Y/N")
    if showMe.lower() =="y":
        print(unique_list)
    
def newRandom():
    if len(unique_list) > 0:
        wichOne = input("Wich list do you want to search? Sorted or un-sorted?      ")
        if whichOne.lower() == "sorted":
            print(unique_list[random.randit(0, len(unique_list)-1)])
        else:
            print(myList[random.randit(0, len(myList)-1)])
    else:
        print(myList[random.randit(0, len(myList)-1)])

def randomSearch():
    print("Why doyou chosie this ")
    print(myList[random.randit(0, len(myList)-1)])

def linerSearch():
    print("WE'er going to go through this list one item at a time!")
    searchValue = input("What are you looking for?    ")
    for x in range(len(myList)):
        if  myList[x] == int(searchValue):
             print("Your item is at index postion  {}".format(x))
        

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index postion{}".format(mid))
            return mid
        elif unique_list[mid]  > x:
            return recursiveBinarySearch(unique_list, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
     else:
         print("Your number isn't here!")


def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] <x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1



def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index postion here:     ")
    print(myList[int(indexPos)])

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        wichOne = input("Wich list do you want to see? Sorted or un-sorted?  ")
        if wichOne.lower() == "sorted":
            print(unique_list)


if __name__== "__main__":
    mainProgram()



