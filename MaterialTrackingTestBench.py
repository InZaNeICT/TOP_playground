import random
import sys
import keyboard
import os



# DONT TOUCH #
def saveToDatabase(input):
    return random.random() > 0.5

def getTag() -> int:
    if random.random() > 0.9:
        return random.randint(10000, sys.maxsize)
    else:
        return None
# DONT TOUCH #
def rfidtagtest():
    run = True
    print("Please press enter to fetch a tag")
    while run:
        try:
            if keyboard.is_pressed("Enter"):
                rfid = getTag()
            if rfid:
                print("Congratulations, rfid-tag was found")
                saveToDatabase
                print("Your tag is being saved to database")
                return True
            else:
                print("Sorry, rfid was not found")
        except: 
            pass

def Questions():
    run = True
    yes = {'y'}
    no = {'n'}
    while run:
        try:
            print("Did the test succeed [y/n]?")
            choice = input().lower()
            if choice in yes:
                os.system('cls')
            elif choice in no:
                return
            print("Are you sure [y/n]?")
            if choice in yes:
                run = False
            elif choice in no:
                    return
        except:
            return
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
