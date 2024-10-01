"""
Module for functions pretaining to managing (modifying) tasks
"""
import task as t

#function for adding a task and setting a priority level
def addtask():   
    while True:
        task_name = input ('Please enter the name of the task or enter "back" to return to the main menu: ')
        if task_name == 'back':
            return []
        break
    while True:   
        task_priority = input ('''
What level of priority is the task?
Please enter "high" for high, "medium" for medium and "low" for low: ''')
        if task_priority == 'high' or task_priority == 'medium' or task_priority == 'low':
            break    
        else:
            print ('Sorry, I don\'t recognize this command. Please try again.')
            continue
    print ('New task successfully added.')
    return [task_name,task_priority,'incomplete']


#function for deleting a task
def deletetask(task_list):    
    while True:
        t.viewtask(task_list)
        delete_task = input('''
Please enter the name of the task you would like to delete or enter "back" to return to the main menu: ''')
        pre_del_len = len(task_list)
        if delete_task == 'back':
            return task_list
        for task in task_list:
            if delete_task == task[0]:
                task_list.remove(task)
                print(delete_task, 'has been successfully removed.')        
        if pre_del_len == len(task_list):
            print ('This task does not exist within the current tasks. Please try again.')
            continue
        break
    return task_list


#function for updating task completion
def taskupdate(task_list):
    while True:
        t.viewtask(task_list)
        update_task = input('''
Please enter the name of the task you would like to update completion for or enter "back" to return to the main menu: ''')       
        if update_task == 'back':   #command to let user go back if they don't want to mark completion anymore
            return task_list
        for task in task_list:  #go through the list and look for the task that user wants to modify
            if update_task == task[0]:                  
                task[2] = 'completed'
                print (update_task, 'has been marked as completed.')
        counter = 0
        for task in task_list:
            if update_task != task[0]:
                counter += 1
        if counter == len(task_list):
            print('This task does not exist. Please try again')
            continue    
        break
    return task_list   

#function to modify task priority
def taskprio(task_list):    
    while True:
        t.viewtask(task_list)
        modify_task = input('''
Please enter the name of the task you would like to modify priority for or enter "back" to return to the main menu: ''')       
        if modify_task == 'back':   #command to let user go back if they don't want to modify 
            return task_list
        for task in task_list:  #go through the list and look for the task that user wants to modify
            if modify_task == task[0]:  
                print ('The', task[0], 'task is currently', task[1], 'priority. What level would you like to change it to?')
                while True:
                    new_prio = input('Please enter "high" for high, "medium" for medium and "low" for low: ')
                    if new_prio == task[1]:     #for if the new priority is the same as before
                        print ('Sorry, this is the same priority level as before. Please enter a new priority level')
                        continue
                    elif new_prio == 'high' or new_prio == 'medium' or new_prio == 'low':
                        task[1] = new_prio      #changing the former priority level to the new priority level
                        break
                    else:
                        print ('Sorry, I don\'t recognize this command. Please try again.')
                        continue    #if user gives incorrect command
        counter = 0
        for task in task_list:
            if modify_task != task[0]:
                counter += 1
        if counter == len(task_list):
            print('This task does not exist. Please try again')
            continue    
        break  
    return task_list


#test
#testlist = [['1','low','3'],['4','medium','6'],['7','high','9']] 
#taskprio(testlist)
#print(testlist)

