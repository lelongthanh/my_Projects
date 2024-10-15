tasks = []


def addTask():
    task = input("Today\'s task: ")
    tasks.append(task)
    print(f'Your task was added')


def listTask():
    if not tasks:
        print('Empty')
    else:
        print('List of tasks: ')
    for index, name_task in enumerate(tasks):
        print(f'Task {index}: {name_task}')


def delTask():
    listTask()
    taskToDelete = int(input('Enter the task number: '))
    if taskToDelete < len(tasks):
        tasks.pop(taskToDelete)
        print(f'Task {taskToDelete} has been deleted')
    else:
        print('Invalid input!')


while True:
    print('=====Welcome=====')
    print('Your life is better when your day is built better')
    print('1: Add task')
    print('2: List of tasks')
    print('3: Delete task')
    print('4: Quit')

    choose = int(input('Your number is: '))

    if choose == 1:
        addTask()

    elif choose == 2:
        listTask()

    elif choose == 3:
        delTask()

    elif choose == 4:
        break

    else:
        print('Invalid Values!')

print('Bye Bye. See you later!')
