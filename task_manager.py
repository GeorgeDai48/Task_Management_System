"""
Module for functions pretaining to managing tasks
"""

#function for adding a task and setting a priority level
def addtask():   
    task_name = input ('Please enter the name of the task ')
    while True:   
        task_priority = input ('''What level of priority is the task?
Please enter "h" for high, "m" for medium and "l" for low ''')
        if task_priority == 'h':
            task_priority = 3
            break
        elif task_priority == 'm':
            task_priority == 2
            break
        elif task_priority == 'l':
            task_priority == 1
            break
        else:
            print ('Sorry, I don\'t recognize this command. Please try again.')
            continue
    print ('New task successfully added.')
    return [task_name,task_priority,1]


