import random
import sys
import keyboard
import os
import time



# DONT TOUCH #
def saveToDatabase(input):
    return random.random() > 0.5

def getTag() -> int:
    if random.random() > 0.9:
        return random.randint(10000, sys.maxsize)
    else:
        return None
# DONT TOUCH #
# Hakee ID:n kun painetaan enteriä, jos ID:tä ei löydetä niin jatketaan sen etsimistä, tallennetaan ID tietokantaan.#
# Painetaan enter -> etsitaan tagi -> tarkistetaan tagi -> tallennetaan tagi
'''
painetaan enter:
    etsitaan tagi
    if tag:
        tallennetaan taki
'''
def rfidtagtest():
    run = True
    print("Please press enter to fetch a tag")
    while run:
        if keyboard.is_pressed("Enter"):
            time.sleep(0.3)
            rfid = getTag()
            if rfid:
                time.sleep(1)
                print("Congratulations, rfid-tag was found")
                time.sleep(1)
                saveToDatabase
                print("Your tag is being saved to database")
                time.sleep(1)
                return True
            else:
                print("Sorry, rfid was not found")


def Questions():
    run1 = True
    yes = {'y'}
    no = {'n'}
    while run1:
        try:
            os.system('cls')
            print("Did the test succeed [y/n]?")
            choice = input().lower()
            if choice in yes:
                os.system('cls')
                print("Nice")
                run1 = False
            elif choice in no:
                return
        except:
            return
    run2 = True
    while run2:
        try:
            print("Are you sure [y/n]?")
            choice = input().lower()
            if choice in yes:
                run2 = False
            elif choice in no:
                    return
        except:
            print("Your answer is saved to database")
            saveToDatabase()
'''
    while True:
        try:
            os.system('cls')
            print("Are you sure [y/n]?")
            if choice in yes:
                pass
            elif choice in no:
                return
        except:
            print("Your answer is saved to database")
            saveToDatabase()
'''''''''



# MAIN PROGRAM
run = True
while run:
    rfidtagtest()
    Questions()
    run = False
    pass

    

    


    
        
# MAIN PROGRAM
# YOUR CODE HERE #

''''''
'''''''''
TIPS:
python keypress:
https://java2blog.com/detect-keypress-python/
python user input:
https://www.w3schools.com/python/ref_func_input.asp
'''
