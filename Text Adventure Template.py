#name: Dylan Grove
#date: 9/15/2016
#description: text based adventure game about a stanger on the street.

import random
import time



def displayIntro():
    print("It's a breezy day in Fall of 1999 and you are walking down the street to the local market.")
    time.sleep(3)
    print("An oddly dressed man is leaning on a bus bench smoking with a smirk on his face as you approach him.")
    print()
    time.sleep(3)
    print("Stranger: It's been a long time since I last saw your face friend.")
    print()
    time.sleep(2)



def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("What do you say?:\n1) Who are you?\n2) I don't have any change.\n")
               
    return path



def checkPath(chosenPath):
   
    correctPath = 1

    if chosenPath == str(correctPath):
        print("Stranger: You know exactly who I am. My name is Don Farraway and you owe me $100,000...")
        time.sleep(2)
        print("         Dr.Anderson")
    else:
        print("Don't pretend you don't know me...")
        time.sleep(2)
        print("         Dr.Anderson")

def choosePathR1():
    if chosenPath == 1 or 2:
        path = ""
        while path != "1" and path != "2":
            path = input("What do you say?\n1)I've never even seen you before in my life!\n2)*Attempt to run*\n")

     


displayIntro()
choice = choosePath()
checkPath(choice) # choice is 1 or 2
choosePath()
choosePathR1()
