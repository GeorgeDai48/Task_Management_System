"""
The main module that the user interacts with.
"""

#importing the task_manager.py and task.py modules 
import task_manager as tm
import task as t

task_list = []

#The welcome text 
print ('''
Welcome to the Task Manager System
In this system, you can add and delete tasks, view tasks, set priority of tasks and mark completion of tasks.''')

#loop to allow the user to return to the main menu after each task (adding, viewing, etc) 
while True:
    main_menu_nav = input('''
You are at the main menu.

Enter "add" to add new tasks
Enter "view" to view existing tasks
Enter "delete" to delete an existing task
Enter "priority" to modify the priority level of an existing task
Enter "update" to update completion status of tasks
Enter "exit" to exit the program
What would you like to do? ''')
    #The adding tasks menu. Includes ability to keep adding tasks until finished, then returns to main menu.
    if main_menu_nav == 'add':
        print ('''
This is the adding tasks menu. Please note that new tasks will be defaulted as incomplete''')
        while True:
            #Calls upon the addtask funtion in the task_manager.py module
            new_items = tm.addtask()
            if new_items == []:
                print ('No new tasks added.')
            else:
                task_list.append(new_items)            
            continue_adding = input ('Would you like to continue adding tasks? Enter "y" for yes, "n" for no. ')
            if continue_adding == 'y':
                continue
            elif continue_adding == 'n':
                break
            else:
                print ('Sorry, I don\'t recognize this command. Please try again.')
                continue

    #The viewing tasks menu, calls upon the viewtask function in the task.py module 
    elif main_menu_nav == 'view':
        t.viewtask(task_list)
        continue

    #Deleting tasks menu, calls delete task funtion in the task_manager.py module
    elif main_menu_nav == 'delete':
        print ('''
This is the deleting tasks menu.''')
        while True:
            task_list = tm.deletetask(task_list)            
            continue_deleting = input ('Would you like to continue deleting tasks? Enter "y" for yes, "n" for no. ')
            if continue_deleting == 'y':
                continue
            elif continue_deleting == 'n':
                break
            else:
                print ('Sorry, I don\'t recognize this command. Please try again.')
                continue

    #modify the priority level of exisiting tasks
    elif main_menu_nav == 'priority':
        #to do
        continue

    #update completetion status of exisiting tasks
    elif main_menu_nav == 'update':
        #to do
        continue

    #Exit program command with asking for confirmation
    elif main_menu_nav == 'exit':        
        while True:
            exit_confirm = input ('''
Are you sure you want to exit? Progress will not be saved. Enter "y" for yes, "n" for no. ''')
            if exit_confirm == 'y':
                print ('Thank you for using the Task Manager System, goodbye.')
                exit()
            elif exit_confirm == 'n':
                break
            else:
                print ('Sorry, I don\'t recognize this command. Please try again.')
                continue
            continue
    else:
        print ('Sorry, I don\'t recognize this command. Please try again.')
        continue


