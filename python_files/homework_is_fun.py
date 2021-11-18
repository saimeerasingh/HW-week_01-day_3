home_work = input('Do you have homework to do? ')
def get_homework(home_work):
    if home_work == 'Yes':
        return "Do your Homework!"
    else:
        return "Take rest!"
print(get_homework(home_work))