class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def is_completed(self):
        return self.completed

    def complete_task(self):
        self.completed = True

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same"
        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same"
        self.due_date = new_date
        return new_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        # if comment_number not in range(len(self.comments)):
        #     return "Cannot find comment"
        # self.comments[comment_number] = new_comment
        # return ", ".join(self.comments)
        try:
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        except IndexError:
            return "Cannot find comment"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def filter_completed_tasks(self):
        return [task for task in self.tasks if task.is_completed()]

    def filter_tasks_by_name(self, task_name):
        return [task for task in self.tasks if task.name == task_name]

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        tasks_to_complete = self.filter_tasks_by_name(task_name)
        if not tasks_to_complete:
            return f"Could not find task with the name {task_name}"
        for task in tasks_to_complete:
            task.complete_task()
        return f"Completed tasks {', '.join([task.name for task in tasks_to_complete])}"

    def clean_section(self):
        completed_tasks = self.filter_completed_tasks()
        self.tasks = [t for t in self.tasks if t not in completed_tasks]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        lines = [f"Section {self.name}:"]
        for task in self.tasks:
            lines.append(task.details())
        return '\n'.join(lines)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
third_task = Task("Go out", "27/05/20axz20")
section.add_task(second_task)
section.add_task(third_task)
# print(section.complete_task("Make bed"))
# print(section.complete_task("Go out"))
print(section.clean_section())
print(section.view_section())
