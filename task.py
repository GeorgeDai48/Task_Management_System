"""
Module for functions pretaining to viewing tasks
"""

#viewing tasks function
def viewtask(task_list):
    print()
    if task_list == []:
        print('''
There are currently no tasks, returning to main menu.''')
    else:
        print('Your current tasks are:')
        for i in task_list:
            print (i[0], ',', (i[1]), 'priority,', i[2])


