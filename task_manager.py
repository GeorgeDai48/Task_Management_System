"""
Module for any functions that modify task_list (the list that contains all the tasks).
"""
import task as t

#Function for adding a task and setting a priority level.
def addtask():   
    while True:
        #Has user enter new task and assigns it to task_name or if they changed their mind, back to cancel the operation and return to the main menu with an empty list.
        task_name = input ('Please enter the name of the task or enter "back" to return to the main menu: ')    
        if task_name == 'back':
            return []
        break
    while True:   
        #Asks user to set priority of the new task and assigns it to task_priority.
        task_priority = input ('''
What level of priority is the task?
Please enter "high" for high, "medium" for medium and "low" for low: ''')
        if task_priority == 'high' or task_priority == 'medium' or task_priority == 'low':
            break    
        else:
            print ('Sorry, I don\'t recognize this command. Please try again.')
            continue
    print ('New task successfully added.')
    #Returns the name, priority and completion status (default incomplete) as a list.
    return [task_name,task_priority,'incomplete']


#Function for deleting a task.
def deletetask(task_list):    
    while True:
        #Calls upon the viewtask function to display all the current tasks for the user before asking them to choose which to delete. 
        t.viewtask(task_list)
        #Assigns the name of the task the user wants to delete to delete_select or if they changed their mind, "back" to cancel the operation and return to the main menu.
        delete_select = input ('''
Please enter the name of the task you would like to delete or enter "back" to return to the main menu: ''')
        #Sets pre_del_len as the length before deleting tasks, will be used in line 46.
        pre_del_len = len (task_list)
        if delete_select == 'back':
            return task_list
        for task in task_list:
            if delete_select == task [0]:
                task_list.remove(task)
                print (delete_select, 'has been successfully removed.')        
        #Tests if the length after deleting a task is the same as before. If it is the same, then the delete_select wasn't in the task list and prompts user to try again.      
        if pre_del_len == len (task_list):
            print ('This task does not exist within the current tasks. Please try again.')
            continue
        break
    return task_list


#Function for updating task completion.
def taskupdate(task_list):
    while True:
        #Calls upon the viewtask function to display all the current tasks for the user before asking them to choose which to update.
        t.viewtask(task_list)
        #Assigns the name of the task the user wants to delete to update_task or if they changed their mind, "back" to cancel the operation and return to the main menu.
        update_task = input ('''
Please enter the name of the task you would like to update completion for or enter "back" to return to the main menu: ''')       
        if update_task == 'back':   
            return task_list
        #Goes through the list and checks if position [0] in the each list within task_list matches the task the user wants to update.
        for task in task_list:  
            if update_task == task [0]:                  
                task [2] = 'completed'
                print (update_task, 'has been marked as completed.')
        #Sets up a counter, initially 0, to count each time the name of a task in task_list fails to match update_task. 
        counter = 0
        for task in task_list:
            if update_task != task [0]:
                counter += 1
        #If the length of task_list is the same as the counter, then no tasks were updated, meaning the user given task does not exist.
        if counter == len (task_list):
            print('This task does not exist. Please try again')
            continue    
        break
    return task_list   

#Function to modify task priority.
def taskprio(task_list):    
    while True:
        #Calls upon the viewtask function to display all the current tasks for the user before asking them to choose which to modify priority.
        t.viewtask(task_list)
        #Assigns the name of the task the user wants to modify priority as modify_task or if they changed their mind, "back" to cancel the operation and return to the main menu.
        modify_task = input ('''
Please enter the name of the task you would like to modify priority for or enter "back" to return to the main menu: ''')       
        if modify_task == 'back':   
            return task_list
        #Goes through the list and checks if position [0] in the each list within task_list matches the task the user wants to modify priority.
        for task in task_list:  
            if modify_task == task [0]:  
                print ('The', task [0], 'task is currently', task [1], 'priority. What level would you like to change it to?')
                #A loop in case the user tries to change priority to the same value as before or if they enter an unrecognized command.
                while True:
                    new_prio = input('Please enter "high" for high, "medium" for medium and "low" for low: ')
                    if new_prio == task [1]:     
                        print ('Sorry, this is the same priority level as before. Please enter a new priority level')
                        continue
                    elif new_prio == 'high' or new_prio == 'medium' or new_prio == 'low':
                        task [1] = new_prio      
                        break
                    else:
                        print ('Sorry, I don\'t recognize this command. Please try again.')
                        continue    
        #Sets up a counter, initially 0, to count each time the name of a task in task_list fails to match modify_task. 
        counter = 0
        for task in task_list:
            if modify_task != task [0]:
                counter += 1
        #If the length of task_list is the same as the counter, then no task priorities were updated, meaning the user given task does not exist.
        if counter == len (task_list):
            print('This task does not exist. Please try again')
            continue    
        break  
    return task_list


