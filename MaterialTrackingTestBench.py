import random
import sys
<<<<<<< HEAD
import keyboard
=======
# import keyboard


>>>>>>> bb48d50380aeb05360212b1d19863706f866b63e

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
<<<<<<< HEAD
                print(id)
            if id:
                print("rfid Tag Was Found")
=======
            if id:
                print("rfid was found")
>>>>>>> bb48d50380aeb05360212b1d19863706f866b63e
                saveToDatabase()
                print("Saving to database")
                return True
            else:
<<<<<<< HEAD
                print("rfid tag not found")
=======
                print("rfid not found")
>>>>>>> bb48d50380aeb05360212b1d19863706f866b63e
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
<<<<<<< HEAD
                    return True
                elif choice in no:
                    return
            elif choice in no:
                return True
            print("Your answer is saved to database")
            saveToDatabase()
        except:
            pass
'''
'''
def Saver():
    run = True
'''




# MAIN PROGRAM
run = True
while run:
    rfidtest()
    print("ok")
    
    run = False
=======
                    pass
                elif choice in no:
                    return
            elif choice in no:
                pass
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

    

    

>>>>>>> bb48d50380aeb05360212b1d19863706f866b63e

    
        
# MAIN PROGRAM
# YOUR CODE HERE #


'''
TIPS:
python keypress:
https://java2blog.com/detect-keypress-python/

python user input:
https://www.w3schools.com/python/ref_func_input.asp

'''