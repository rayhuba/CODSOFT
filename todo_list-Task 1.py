# todo_list.py

#1.Add a New Task
def add_task(tasks, title):
    task_id = len(tasks) +1
    task = {
        'id':task_id,
        'title':title,
        'completed':False
    }
    tasks.append(task)
    print(f"Task '{title}' added. ")

#2.View All Tasks 
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for task in tasks:
        status = "Completed" if task ['completed'] else "Not Completed"
        print(f"{task['id']}. {task['title']} - {status}")

#3.Mark a Task as Completed
def mark_completed(tasks,task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task '{task['title']}' marked as completed.")
            return
    print(f"Task with id {task_id} not found.")

#4. Delete a Task
def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print(f"Task '{task['title']}' deleted.")
            return
    print(f"Task with id {task_id} not found.")


#5. Update a Task
def update_task(tasks, task_id, new_title):
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = new_title
            print(f"Task {task_id} updated to '{new_title}'.")
            return
    print(f"Task with id {task_id} not found.")

#Create a Command-Line Interface
def main():
    tasks = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task id to mark as completed: "))
            mark_completed(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task id to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            task_id = int(input("Enter task id to update: "))
            new_title = input("Enter new title: ")
            update_task(tasks, task_id, new_title)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
