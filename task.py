"""
Module for functions that do not modify the task_list
"""

#viewing tasks function.
def viewtask(task_list):
    if task_list == []:
        print ('''
There are currently no tasks, returning to main menu.''')
    else:
        print ('''
Your current tasks are:''')
        #Each list within task_list has the name in the [0] position, priority level in [1] and completion status in [2]. Prints this information out on separate lines.
        for item in task_list:
            print (item [0], ',', (item [1]), 'priority,', item [2])

#Function to run any yes or no questions that the program asks the user.
def yes_no_question(action):
    #Variable flag to be used as a boolean for while loop, in case user inputs an invalid command.
    flag = True
    while flag == True:
        continue_adding = input (f'Would you like to {action} Enter "y" for yes, "n" for no. ') 
        if continue_adding == 'y' or continue_adding == 'Y':
            break
        elif continue_adding == 'n' or continue_adding == 'N':
            flag = False
        else:
            print ('Sorry, I don\'t recognize this command. Please try again.')     
            continue
    else:
        return "n"    