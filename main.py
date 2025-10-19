import os
import array
mainArray = []
def viewArray():
    os.system("cls")
    print(mainArray)

def addElement(element : float):
    os.system("cls")
    mainArray.append(element)
    print(str(element)," has been added to the array!")

def removeElement(element : float):
    os.system("cls")
    mainArray.remove(element)
    print(str(element)," has been removed to the array!")

def sumArray():
    os.system("cls")
    finalSum = sum(mainArray)
    print("Sum: ",finalSum)

def averageElements():
    os.system("cls")
    finalSum = sum(mainArray)
    finalSum = finalSum/len(mainArray)
    print("average: ",finalSum)

def minmax():
    os.system("cls")
    minE = min(mainArray)
    maxE = max(mainArray)
    print("Minimum: ",minE)
    print("Max: ",maxE)

def reverseArray():
    os.system("cls")
    mainArray.reverse()
    print("Array Reversed")
def searchElement(element : float):
    if element in mainArray:
        print(str(element), " is found at the index ", mainArray.index(element))
    else:
        print(str(element), " is not on the array")

def main():
    running = True
    while running:
        print("===BEA ARRAY OPERATION===\n[1]View Array\n[2]Add Element\n[3]Remove Element\n[4]Sum of Elements\n[5]Average of all Elements\n[6]Minimum and Maximum\n[7]Reverse Array\n[8]Search\n[9]End program")
        choiceMain = input("Choice: ")
        if choiceMain == '1':
            viewArray()
        elif choiceMain == '2':
            element = float(input('Enter element to add: '))
            addElement(element)
        elif choiceMain == '3':
            element = float(input('Enter element to remove: '))
            removeElement(element)
        elif choiceMain == '4':
            sumArray()
        elif choiceMain == '5':
            averageElements()
        elif choiceMain == '6':
            minmax()
        elif choiceMain == '7':
            reverseArray()
        elif choiceMain == '8':
            if len(mainArray) == 0:
                print("No Elements present in the array add one first!")
            else:
                element = float(input('Enter element to search: '))
                searchElement(element)
        elif choiceMain == '9':
            os.system("cls")
            print("Thanks For Using! Magsukul!")
            running = False
        

        
if __name__ == "__main__":
    main()