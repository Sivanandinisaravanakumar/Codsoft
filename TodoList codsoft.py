class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = '✔ ' + self.tasks[task_index]

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\n== TO-DO LIST ==")
        print("1. Add Task")
        print("2.Mark Task as Completed ")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task:")
            todo_list.add_task(task)
            print("Task added Successfully.")
        elif choice == '2':
            todo_list.display_tasks()
            task_index=int(input("Enter the index of the task to mark as completed:")) -1
            todo_list.mark_completed(task_index)
            print("Task marked as completed.")
        elif choice == '3':
            todo_list.display_tasks()
            task_index=int(input("Enter the index of the task to delete:")) -1
            todo_list.delete_task(task_index)
            print("Task deleted Successfully.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.Please Try again.")
if __name__ == "__main__":
    main()        



            



