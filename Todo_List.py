#creating an empty list to store tasks
todo_list = []

# Function for adding a new task
def add_task():
    task = input("Enter a task : ")
    todo_list.append({"Task":task , "Status": "pending"})
    print("New Task Added Successfully!")

#Function for view all tasks
def view_task() :
    print("Your Todo List :")
    if len(todo_list) == 0 :
        print("No pending tasks!")
    else :
        for index, task in enumerate(todo_list ,1) :
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

#Function for removing a task
def remove_task() :
    if len(todo_list) == 0 :
        print("List is empty")
    else:
        try:
            search_index = int (input("Enter the task number that you want to remove:"))
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid . Please enter a valid task number.")

        
# function for task mark done
def mark_done():
        if len(todo_list) == 0 :
            print("List is empty")
        else:
            try:
                search_index = int (input("Enter the task number that you want to mark as complete:"))
                if 0 <= search_index < len(todo_list):
                    todo_list[search_index]['Status'] = 'done'
                    print(f"Task {todo_list[search_index]['Task']}has been marked as Done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print(" Please enter a valid task number.")

#Function for displaying menu
def menu() :
    while True:
        print("*** Main Menu ***")
        print(" 1. Add the task")
        print(" 2. View All tasks")
        print(" 3. Remove the task")
        print(" 4. Mark the task as done")
        print(" 5. Exit")
 
        choice = int(input("Enter your choice:"))
        if  choice == 1 :
            add_task()
        elif choice == 2 :
            view_task() #type: ignore
        elif choice == 3:
            remove_task()  #type: ignore
        elif choice == 4 : 
            mark_done()  #type: ignore
        elif choice == 5:   
            print("Exiting the Application ..") 
            exit()
        else :
            print("Invalid choice! Try again")

menu()
      
