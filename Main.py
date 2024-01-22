# Task manager

def createNewTask():
    print("Create New Task")
    
def viewAllTasks():
    print("View All Task")
    
def removeATask():
    print("Remove A Task")

def Main():
    while (True):
        # Promt the user with the main options
        userInput = input("What would you like to do?\n   [1] Create New Task\n   [2] View All Tasks\n   [3] Remove A Task\n>")
        # Validity Check
        if (userInput.isnumeric() == False):
            print("\n\n\nPlease input a valid number choice from the list provided!")
            continue
        elif (int(userInput) >= 4):
            print("\n\n\nSorry! There was no option 4 on the list provided. Please try again!")
            continue
        else:
            match int(userInput):
                case 1:
                    createNewTask()
                case 2:
                    viewAllTasks()
                case 3:
                    removeATask()
                case __:
                    continue
                    
            break
        
Main()