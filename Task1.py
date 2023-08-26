print("\n To do my list")
tasks=[]

def add_task():
    task=input("Enter a new task:")
    tasks.append(task)
    print("task added successfully.")

def view_tasks():
    if len(tasks)==0:
        print("no tasks.")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    if len(tasks)==0:
        print("no task to delete")
    else:
        print('tasks')
        for i ,task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input('Enter the task no delete:'))

        if 0 < choice <=len(tasks):
            del tasks[choice-1]
            print('task deleted successfully.')
        else:
            print('invalid task number')

def update_task(index,new_task): 
    if index<1 or index>len(tasks):
        print("invalid index")
    else:
        tasks[index-1]=new_task
        print("Task updated succesfully!")
        
def main():
    while True:
        print('\n================== To Do List Application ======================')
        print("1. Add task ")
        print('2. view task')
        print('3. delete task')
        print('4. update task')
        print('5.Exit')

        choice=int(input('Enter your choice : '))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            index=int(input("Enter the index of the task to update:"))
            new_task=input("Enter the new task :")
            update_task(index,new_task)
        elif choice == 5:
            print("Thank you for using To Do List Application.")
        else:
            print('Invalid choice. please try again.')

        



if __name__ == "__main__":
    main()