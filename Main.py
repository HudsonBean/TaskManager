# Task manager

#Imports
import os

#Functions
clear = lambda: os.system('clear')


#Classes
class Task: 
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    


#Main

tasks = { }


def createNewTask():
    while (True):
        userInput = input("What will the name of the new task be?\n>")
        # Validity check
        if (len(userInput) <= 0): 
            print("Please provide a valid name for the task!\n\n\n")
            continue;
        else:
            taskName = userInput;
            while (True):
                userInput = input("What is the priority of '" + taskName + "'?\n>")
                # Validity check
                if (len(userInput) <= 0 or userInput.isnumeric() == False or int(userInput) <= 0):
                    print("Please provide a valid number for the priority. 1 being first priority!")
                    continue
                else:
                    # Create new task
                    tasks[taskName] = Task(taskName, userInput)
                    clear()
                    Main()
                    break;
            break;
    # print(taskName + " !")             
    
def viewAllTasks():
    print("View All Task")
    
def removeATask():
    print("Remove A Task")
    
def verify(option):
    while (True):
        userInput = input("You have selected to " + option + ". Is this correct?\nY/N >")
        if (userInput.isalpha == False):
            # Check if is alpha
            print("Please provide option choice 'Y' to signify yes or 'N' to signify no.")
            continue
        else:
            # check options
            match userInput.lower():
                case "y" | "yes":
                    return True
                case "n" | "no":
                    return False
                

def Main():
    while (True):
        # Promt the user with the main options
        userInput = input("What would you like to do?\n   [1] Create New Task\n   [2] View All Tasks\n   [3] Remove A Task\n>")
        # Validity Check
        if (userInput.isnumeric() == False):
            print("\n\n\nPlease input a valid number choice from the list provided!")
            continue
        # Second validity check
        elif (int(userInput) >= 4):
            print("\n\n\nSorry! There was no option 4 on the list provided. Please try again!")
            continue
        else:
            # Case statemnet to check options
            match int(userInput):
                case 1:
                    # Verify
                    if (verify("'Create New Task'") == False):
                        continue
                    else:
                        createNewTask()
                case 2:
                    
                    if (verify("'View All Tasks'") == False):
                        continue
                    else:
                        viewAllTasks()
                case 3:
                    
                    if (verify("'Remove A Tasks'") == False):
                        continue
                    else:
                        removeATask()
                    
            break
        
Main()