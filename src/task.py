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