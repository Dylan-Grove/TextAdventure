#--------------------TextAdventure Module--------------------#
#----------------------By: Dylan Grove-----------------------#

#READ ME#
# Copy this file to the same folder as your project to import
# For best import use the following command:
# from TextAdventure import ts, ps, pc, etc, rng, playagain, path2, path3, path4
# This removes the need for TextAdventure.ts(x) or TextAdventure.ps(" ")
# and now becomes ts(x) or ps(" ")


#------------------------------------------------------------
# Imports #
# Required to make the following functions run
#------------------------------------------------------------
import sys
import time
import random


#------------------------------------------------------------
# Time sleep #
# Allows you to input a pause in seconds as x.
#------------------------------------------------------------
def ts(x):
    time.sleep(x)



#------------------------------------------------------------
# Print Slow Configurable #
# Allows you to print a string as if someone were typing it.

# Also allows you to change the speed with x
# Default (0.03)    -    higher value = slower speed

# Also Allows you to print on the same line as the last ps
# Default (1)
# y = 1    -    new line after each ps
# y = 0    -    no new line after each ps
#------------------------------------------------------------
def ps(str, x = 0.03, y = 1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(x)
    def printspace():
        if y == 1:
            print()
        else:
            pass
    printspace()
#------------------------------------------------------------
# Page Clear #
# Allows you to clear the interpreter.
#------------------------------------------------------------
def pc():                                                                               
    for full in range(50):
        print()



#------------------------------------------------------------
# Enter To Continue #
# Creates a prompt that will wait for a user to hit enter
# before continuing with the code.
#------------------------------------------------------------
def etc():
    ts(.5)
    input("\n[Press enter to continue...]\n")



#------------------------------------------------------------
# Random Number Generator #
# Randomly returns a number between and including x to y
#------------------------------------------------------------
def rng(x, y):
    z = random.randint(x, y)
    return z



#------------------------------------------------------------
# Play Again #
# Used to restart code from a certain point or end it based
# on what the user inputs after "ps(askstring)"

# A 3 variable function that requires the following to work:

# askstring    -  The words printed to the user at the start of the function
#              -  This is optional and the default is 'Would you like to play again?'

# yesfunction  -  function run if the user inputs yes or y
# yesstring    -  Optional String printed to the user before yesfunction is run

# nofunction   -  function run if the user inputs no or n
# nostring     -  Optional String printed to the user before nofunction is run

# ex.1 -  pa(function1, function2)
# ex.2 -  pa(function1, function2, yesstring = "You entered yes", nostring = "You entered no", askstring = "What will you do next?")
#------------------------------------------------------------
def playagain(yesfunction, nofunction, yesstring = " ", nostring = " ", askstring = 'Would you like to play again?'):
    ps(askstring)
    playagain = input("---> ")
    if playagain == "yes" or playagain == "y":
        ps(yesstring)
        ts(1)
        yesfunction()
    elif playagain == "no" or playagain == "n":
        ps(nostring)
        ts(1)
        nofunction()
    else:
        ps("That's an invalid option. Try again.")
        ts(1)
        playagain(yesfunction, nofunction, yesstring, nostring, askstring = 'Would you like to play again?')
        
        
        
#------------------------------------------------------------
# 2 Option Path #
# Used to create a path in the adventure.
# Only works with user options A or B

# A 6 variable function that requires the following to work:

# askstring1                -  the initial question for the path. ex. "Where will you go?"
# askstring2                -  Where options are presented. ex. "A)path1 \nB)path2"

# pathfunction(1, 2)        -  leads to selected path (Must be defined)

# optionalstring(1, 2, 3)   -  optional, used before askstring1 to display more info

# ex. path2("Where will you go?", "A)path1 \nB)path2", p1, p2)
#------------------------------------------------------------
def path2(askstring1, askstring2, pathfunction1, pathfunction2, optionalstring1 = '', optionalstring2 = '', optionalstring3 = ''):
    
    if optionalstring1 != '' or optionalstring2 != '' or optionalstring3 != '':
        ps(optionalstring1)
        ps(optionalstring2)
        ps(optionalstring3)
    else:
        pass
    
    ps(askstring1)
    ps(askstring2)
    
    pathinput = input("---> ")
    if pathinput == "a":
        ts(1)
        pathfunction1()
    elif pathinput == "b":
        ts(1)
        pathfunction2()
    else:
        ps("That's an invalid option. Try again.")
        ts(1)
        path2(askstring1, askstring2, pathfunction1, pathfunction2, optionalstring1, optionalstring2, optionalstring3)
        
        
#------------------------------------------------------------
# 3 Option Path #
# Used to create a path in the adventure.
# Only works with user options A, B or C

# A 7 variable function that requires the following to work:

# askstring1                -  The initial question for the path. ex. "Where will you go?"
# askstring2                -  Where options are presented. ex. "A)path1 \nB)path2 \nC)path3"

# pathfunction(1, 2, 3)     -  Leads to selected path (Must be defined)

# optionalstring(1, 2, 3)   -  Optional, used before askstring1 to display more info
#                           -  Will not be printed unless as string is in OS1

# ex. path3("Where will you go?", "A)path1 \nB)path2 \nC)path3", p1, p2, p3)
#------------------------------------------------------------
def path3(askstring1, askstring2, pathfunction1, pathfunction2, pathfunction3, optionalstring1 = '', optionalstring2 = '', optionalstring3 = ''):
    
    if optionalstring1 != '' or optionalstring2 != '' or optionalstring3 != '':
        ps(optionalstring1)
        ps(optionalstring2)
        ps(optionalstring3)
    else:
        pass
    
    ps(askstring1)
    ps(askstring2)
    
    pathinput = input("---> ")
    if pathinput == "a":
        ts(1)
        pathfunction1()
    elif pathinput == "b":
        ts(1)
        pathfunction2()
    elif pathinput == "c":
        ts(1)
        pathfunction3()
    elif pathinput == "d":
        ts(1)
        pathfunction4()
    else:
        ps("That's an invalid option. Try again.")
        ts(1)
        path3(askstring1, askstring2, pathfunction1, pathfunction2, pathfunction3, optionalstring1, optionalstring2, optionalstring3)
        
        
        
#------------------------------------------------------------
# 4 Option Path #
# Used to create a path in the adventure.
# Only works with user options A, B, C, and D

# A 8 variable function that requires the following to work:

# askstring1                -  the initial question for the path. ex. "Where will you go?"
# askstring2                -  Where options are presented. ex. "A)path1 \nB)path2 \nC)path3 \nD)path4"

# pathfunction(1, 2, 3, 4)  -  leads to selected path (Must be defined)

# optionalstring(1, 2)      -  optional, used before askstring1 to display more info

# ex. path4("Where will you go?", "A)path1 \nB)path2 \nC)path3 \nD)path4", p1, p2, p3, p4)
#------------------------------------------------------------
def path4(askstring1, askstring2, pathfunction1, pathfunction2, pathfunction3, pathfunction4, optionalstring1 = '', optionalstring2 = '', optionalstring3 = ''):
    
    if optionalstring1 != '' or optionalstring2 != '' or optionalstring3 != '':
        ps(optionalstring1)
        ps(optionalstring2)
        ps(optionalstring3)
    else:
        pass
    
    ps(askstring1)
    ps(askstring2)
    
    pathinput = input("---> ")
    if pathinput == "a":
        ts(1)
        pathfunction1()
    elif pathinput == "b":
        ts(1)
        pathfunction2()
    elif pathinput == "c":
        ts(1)
        pathfunction3()
    elif pathinput == "d":
        ts(1)
        pathfunction4()
    else:
        ps("That's an invalid option. Try again.")
        ts(1)
        path4(askstring1, askstring2, pathfunction1, pathfunction2, pathfunction3, pathfunction4, optionalstring1, optionalstring2, optionalstring3)
        