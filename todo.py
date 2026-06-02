import sys

def main():
    if len(sys.argv) < 2:
        print("For running this program you need to use the command line\n")
        print("You should use the following command: ")
        print("\tpython todo.py [command]\n")
        print("The available commands are:")
        print("\tadd - Adds a task. Prompts user for task text.")
        print("\tdone - Deletes a task. Prompts user for task id.")
        print("\ttasks - Displays all inputted tasks.")

        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many arguments\n")
        print("You should use the following command: ")
        print("\tpython todo.py [command]\n")

        sys.exit()
    else:
        match sys.argv[1]:
            case "add":
                add()
            case "done":
                done()
            case "tasks":
                tasks()
            case _:
                print("That's and invalid command\n")
                print("The available commands are:")
                print("\tadd - Adds a task. Prompts user for task text.")
                print("\tdone - Deletes a task. Prompts user for task id.")
                print("\ttasks - Displays all inputted tasks.")

                sys.exit()

def add():
    task = input("Task: ")

    if "±±±" in task:
        sys.exit("Invalid task format. Try again")

    indexes = []
    lines = []

    with open("todo.txt") as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    
    if lines[0] != "0":
        for line in lines[1:]:
            num, todo = line.split("±±±")
            indexes.append(num)
            
    with open("todo.txt", "w") as file:
        num_tasks = int(lines[0])

        file.write(str(num_tasks + 1) + "\n")

        if num_tasks == 0:
            file.write("1±±±" + task + "\n")
            print(f"You have added the task: {task}")
        else:
            for line in lines[1:]:
                file.write(line + "\n")

            last_index = int(indexes.pop(len(indexes) - 1))
            file.write(str(last_index + 1) + "±±±" + task + "\n")
        
            print(f"You have added the task: {task}")

def done():
    indexes = []
    lines = []

    with open("todo.txt") as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    
    if lines[0] == "0":
        sys.exit("You don't have tasks to do")
    else:

        id_task = input("Task to mark as done (ID): ")

        for line in lines[1:]:
            num, todo = line.split("±±±")
            indexes.append(num)
    
    if id_task in indexes:
        with open("todo.txt", "w") as file:
            num_tasks = int(lines[0])

            file.write(str(num_tasks - 1) + "\n")

            location_task = indexes.index(id_task)
            
            for i in range(len(lines[1:])):
                
                if i != location_task:
                    file.write(lines[i + 1] + "\n")
                else:
                    task = lines[i + 1]

            print(f"You have marked as done the task: {task.removeprefix(f"{id_task}±±±")}")
    else:
        sys.exit("Any task has that ID")

def tasks():
    lines = []

    with open("todo.txt") as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    
    if lines[0] == "0":
        sys.exit("You don't have tasks to do")
    else:
        print(f"You have {lines[0]} tasks to do:\n")

        for line in lines[1:]:
            num, task = line.split("±±±")
            print(f"ID: {num} - {task}")

if __name__ == "__main__":
    main()