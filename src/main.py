import pyfiglet
def display_banner():
    banner = pyfiglet.figlet_format("Task Manager")
    print(banner)

from task import Task
from manager import TaskManager

manager = TaskManager()
if __name__ == "__main__":
    display_banner()
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
            for i, task in enumerate(tasks, start=1):
                 print(f"[{i}] {task}")

            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index <= len(tasks):
               tasks[index - 1].mark_completed()
               print("Task marked as completed.")
            else:
               print("Invalid task number.")

        elif choice == "5":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks, start=1):
               print(f"[{i}] {task}")
            index_task = int(input("Enter the number of the task to remove: "))
            if 0 <= index_task < len(tasks):
                manager.remove_task(index_task - 1)
                print("Task removed")
            else:
                print("Invalid task number.")
        elif choice == "6":
            manager.save_to_file()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")







