"""
The main module that the user interacts with.
"""

#importing the task_manager.py and task.py modules 
import task_manager as tm
import task as t

task_list = []
print ('''
Welcome to the Task Manager System
In this system, you can add and delete tasks, view tasks, set priority of tasks and mark completion of tasks.''')

while True:
    main_menu_nav = input('''Enter "add" to add new tasks
Enter "view" to view existing tasks
Enter "delete" to delete an existing task
Enter "priority" to modify the priority level of an existing task
Enter "exit" to exit the program
What would you like to do? ''')
    if main_menu_nav == 'add':
        while True:
            task_list += tm.addtask()            
            continue_adding = input ('Would you like to continue adding tasks? Enter "y" for yes, "n" for no. ')
            if continue_adding == 'y':
                continue
            elif continue_adding == 'n':
                break
            else:
                print ('Sorry, I don\'t recognize this command. Please try again.')
                continue
        continue
    elif main_menu_nav == 'view':
        print (task_list)
        continue
    elif main_menu_nav == 'delete':
        #
        continue
    elif main_menu_nav == 'priority':
        #
        continue
    elif main_menu_nav == 'exit':
        #Exit program command with asking for confirmation
        while True:
            exit_confirm = input ('Are you sure you want to exit? Progress will not be saved. Enter "y" for yes, "n" for no. ')
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


