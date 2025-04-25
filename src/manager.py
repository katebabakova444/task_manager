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
