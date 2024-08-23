import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Task List
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=('Helvetica', 18))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Mark Completed Button
        self.mark_completed_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(pady=5)

        # Delete Task Button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Update Task Button
        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            task = {'title': task_title, 'completed': False}
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task['title']} - {status}")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.tasks[idx]['completed'] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.tasks.pop(idx)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            new_title = self.task_entry.get()
            if new_title:
                self.tasks[idx]['title'] = new_title
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "New task title cannot be empty.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
