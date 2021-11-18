
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks

def list_of_incomplete_tasks(list):
    list_of_incomplete_tasks = []
    for task in tasks:
        if task['completed'] == False:
            list_of_incomplete_tasks.append(task)
            
    return list_of_incomplete_tasks       
    
print(list_of_incomplete_tasks(tasks))    

# Print a list of completed tasks

def list_of_completed_tasks(list):
    list_of_completed_tasks = []
    for task in tasks:
        if task['completed'] == True:
            list_of_completed_tasks.append(task)
            
    return list_of_completed_tasks       
    
print(list_of_completed_tasks(tasks))    

# Print a list of all task descriptions

def task_description(list):
    task_description_list = []
    for task in tasks:
        task_description_list.append(task['description'])
    return task_description_list

print(task_description(tasks))

# Print a list of tasks where time_taken is at least a given time

def task_completion_time(time):
    time_taken_above_given_time =[]
    for task in tasks:
        if task['time_taken'] >= time:
          time_taken_above_given_time.append(task)
    return time_taken_above_given_time    

print(task_completion_time(30))

# Print any task with a given description

def get_task(list,task_description):
    found_task = None
    for task in list:
        if task['description'] == task_description:
            found_task = task
    return found_task
    
print(get_task(tasks,'Feed Cat'))

#Given a description update that task to mark it as complete.

def task_complete_update(list,task_name):
    for task in list:
        if task['description'] == task_name:
            if task['completed'] == False:
                task['completed'] = True
            return task
    

print(task_complete_update(tasks,'Wash Dishes'))


def task_complete_update(list,task_name):
    for task in list:
        if task['description'] == task_name and task['completed'] == False:
            task['completed'] = True
            return task
print(task_complete_update(tasks,'Clean Windows'))

#Add a task to the list

def add_new_item(list,new_task):
    for task in list:
       list.append(new_task)
       return list

print(add_new_item(tasks,{'"description": "Water Plants", "completed": True, "time_taken": 30'}))