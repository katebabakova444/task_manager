class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} - {self.description}"
class TaskManager:
    def __init__ (self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def list_tasks(self):
        return self.tasks
    def list_completed(self):
        return [task for task in self.tasks if task.completed]
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    def display_tasks(self, task_list):
        print("===Tasks===")
        if not task_list:
            print("No tasks found.")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
    def display_completed_tasks(self):
        completed = self.list_completed()
        if not completed:
            print("No completed tasks to display.")
        else:
            self.display_tasks(completed)
    def save_to_file(self):
        with open("../task_report.txt", "w") as file:
            file.write("===Task Report===\n\n")
            task_list = self.tasks
            if not task_list:
                print("No tasks available.\n")
            else:
                 for i, task in enumerate(task_list, start=1):
                     status = "[✓]" if task.completed else"[ ]"
                     file.write(f"{i}. {status} {task.title} - {task.description}\n")
        print("Tasks saved to task_report.txt")



manager = TaskManager()
while True:
    print("\nMenu:")
    print("[1] Add task")
    print("[2] Show all tasks")
    print("[3] Show completed tasks")
    print("[4] Mark task as completed")
    print("[5] Remove task")
    print("[6] Save tasks to file")
    print("[7] Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        new_task = Task(title, description)
        manager.add_task(new_task)
    elif choice == "2":
        tasks = manager.list_tasks()
        manager.display_tasks(tasks)
    elif choice == "3":
        manager.display_completed_tasks()
    elif choice == "4":
        tasks = manager.list_tasks()
        for i, task in enumerate(tasks):
            print(f"[{i}] {task}")
        index = int(input("Enter the task number to mark as completed: "))
        if 0 <= index < len(tasks):
           tasks[index].mark_completed()
           print("Task marked as completed.")
        else:
             print("Invalid task number.")
    elif choice == "5":
        tasks = manager.list_tasks()
        for i, task in enumerate(tasks):
            print(f"[{i}] {task}")
        index_task = int(input("Enter the number of the task to remove: "))
        if 0 <= index_task < len(tasks):
            manager.remove_task(index_task)
        else:
            print("Invalid task number.")
    elif choice == "6":
        manager.save_to_file()
    elif choice == "0":
        break







