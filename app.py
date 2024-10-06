"""
The main module that the user interacts with. Contains code for user interaction, navigating through the main menu and calling upon functions from the modules
"""

import task_manager as tm
import task as t

#Creates the list for storing all tasks(initially empty). 
task_list = []  

print ('''
Welcome to the Task Manager System
In this system, you can add and delete tasks, view tasks, set priority of tasks and mark completion of tasks.''')

#loop to allow the user to return to the main menu after each task (adding, viewing, etc). Have main_menu_nav be the user input to navigate the main menu.
while True:
    main_menu_nav = input ('''
You are at the main menu.

Enter "add" to add new tasks
Enter "view" to view existing tasks
Enter "delete" to delete an existing task
Enter "priority" to modify the priority level of an existing task
Enter "update" to update completion status of tasks
Enter "exit" to exit the program
What would you like to do? ''')
    
    #The adding tasks menu. 
    if main_menu_nav == 'add':
        while True:    
            #Calls upon the addtask function and assigns the added tasks as a list to new_items. If the returned list is empty, recognizes that no new tasks were added.
            new_items = tm.addtask(task_list)    
            if new_items == []:                    
                break
            elif new_items == 'na':
                continue
            else:
                #Puts the new_items into task_list, making a nested list. Each nested list contains data on the name, priority level and completion status. 
                task_list.append(new_items) 
            #Call upon yes_no_question function to ask if the user wants to continue adding tasks with continue_adding set to the output.         
            continue_adding = t.yes_no_question("continue adding tasks?")
            if continue_adding == 'n':
                break

    #The viewing tasks menu.
    elif main_menu_nav == 'view':
        #Calls upon the viewtasks function that displays all tasks.
        t.viewtask(task_list)   

    #The deleting tasks menu.
    elif main_menu_nav == 'delete':
        while True:
            if task_list == []: 
                print ('''
There are currently no tasks, returning to main menu.''')
                break
            print ('''
This is the deleting tasks menu.''')        
            #Calls upon the deletetask fuction that deletes tasks and updates the task_list list.
            task_list = tm.deletetask(task_list)    
            #Call upon yes_no_question function to ask if the user wants to continue deleting tasks with continue_deleting set to the output.         
            continue_deleting = t.yes_no_question("continue deleting tasks?")
            if continue_deleting == 'n':
                break

    #Change priority of existing tasks menu.
    elif main_menu_nav == 'priority':
        if task_list == []:     
            print ('''
There are currently no tasks, returning to main menu.''')
            continue
        print ('''
This is the task priority modification menu.''')
        while True:
            #Calls upon taskprio function that modifies task priority and updates the task_list list.
            task_list = tm.taskprio(task_list)     
            #Call upon yes_no_question function to ask if the user wants to continue changing task priority with continue_priority set to the output.         
            continue_priority = t.yes_no_question("continue changing task priority?")
            if continue_priority == 'n':
                break


    #Update task completion menu.
    elif main_menu_nav == 'update':
        if task_list == []:     
            print ('''
There are currently no tasks, returning to main menu.''')       
            continue
        print ('''
This is the updating task completion menu.''')
        while True:
            #Calls upon the taskupdate funtion that updates tasks as complete and updates the task_list list.
            task_list = tm.taskupdate(task_list)    
            #Call upon yes_no_question function to ask if the user wants to continue modifying task completetion status with continue_update set to the output.         
            continue_update = t.yes_no_question("continue updating task completion?")
            if continue_update == 'n':
                break

    #Exit program command with asking for confirmation.
    elif main_menu_nav == 'exit':        
        while True:     
            #Call upon yes_no_question function to ask if the user is sure they want to exit with continue_exiting set to the output.         
            continue_exiting = t.yes_no_question("exit the program? Progress will not be saved.")
            if continue_exiting == 'n':
                break        
            print ('''
Thank you for using the Task Manager System, goodbye.''')
            exit()
            
            
    else:
        #For when the user inputs an unrecognized command in the main menu.
        print ('''
Sorry, I don\'t recognize this command. Please try again.''')     

        continue


