# views.py

from app import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List")
        tasks = manager.list_tasks()
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == "2":
            index = int(input("Enter task number to complete: ")) - 1
            manager.complete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to remove: ")) - 1
            manager.remove_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
