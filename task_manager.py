"""
Module for functions pretaining to managing tasks
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






def deletetask(task_list):    
    while True:
        t.viewtask(task_list)
        delete_task = input('''
Please enter the name of the task you would like to delete or enter "back" to return to the main menu: ''')
        pre_del_len = len(task_list)
        if delete_task == 'back':
            return task_list
        for item in task_list:
            if delete_task in item[0]:
                task_list.remove(item)
                print(delete_task, 'has been successfully removed.')        
        if pre_del_len == len(task_list):
            print ('This task does not exist within the current tasks. Please try again.')
            continue
        break
    return task_list

"""
#function test
task_list = [['1','2','3'],['4','5','6'],['7','8','9']] 
deletetask(task_list)
"""