def task():
    # variable to store the tasks
    tasks =[]

    # welcome message
    print("---- WELCOME  TO THE TASK MANAGEMENT SYSTEM ----")
    
    # asking no. of task want to add  and tasks
    total_tasks =int(input("Enter no of task you want to add : "))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)

    print(f"-- Todays Tasks ---\n{tasks}")

    while True:
        operations =int(input("\nEnter\n1. ADD\n2. UPDATE\n3. DELETE\n4. VIEW\n5. EXIT\n"))
        
        # add task in list
        if operations ==1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been added successfully")

        # update task in list
        elif operations ==2:
            update_Task =input("Enter the task you want to update: ")
            if update_Task in tasks:
                update = input("Enter new task: ")
                index =tasks.index(update_Task)
                tasks[index]=update
                print(f"Updated task {update}...")
            else:
                print(f"{update_Task} not in your list to do")

        # delete task in list        
        elif operations ==3:
            delete_task =input("Enter the task you want to delete: ")
            if delete_task in tasks:
                index =tasks.index(delete_task)
                del tasks[index]
                print(f"Deleted task {delete_task}...")
            else:
                print(f"{delete_task} not in your list to do")
        
        # view the list of tasks
        elif operations ==4:
            print(f"Total Tasks: {tasks}")
        
        # exit from program
        elif operations ==5:
            print("\nSigning off...\nSee you again :)\n")
            break
task()