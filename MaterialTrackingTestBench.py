import random
import sys
# import keyboard



# DONT TOUCH #
def saveToDatabase(input):
    return random.random() > 0.5

def getTag() -> int:
    if random.random() > 0.9:
        return random.randint(10000, sys.maxint)
    else:
        return None
# DONT TOUCH #
''''
# YOUR CODE HERE #
def rfidtest():
    run = True
    while run:
        try:
            print("press enter to ask If rfid was found")
            if keyboard.is_pressed("Enter"):
                id = getTag()
            if id:
                print("rfid was found")
                saveToDatabase()
                print("Saving to database")
                return True
            else:
                print("rfid not found")
                pass
        except:
            pass
'''
def Questions():
    run = True
    yes = {'y'}
    no = {'n'}
    while run:
        try:
            print("Did the test succeed [y/n]?")
            choice = input().lower()
            if choice in yes:
                print("are you sure [y/n]?")
                if choice in yes:
                    print("homo")
                elif choice in no:
                    return
            elif choice in no:
               print("olet neekeri")
        except:
            print("Your answer is saved to database")
            saveToDatabase()
'''
def Saver():
    run = True
    
'''
# MAIN PROGRAM
run = True
while run:
    if Questions():
        print("xd")
        run = False

    

    


    
        
# MAIN PROGRAM
# YOUR CODE HERE #

'''
TIPS:
python keypress:
https://java2blog.com/detect-keypress-python/

python user input:
https://www.w3schools.com/python/ref_func_input.asp

'''