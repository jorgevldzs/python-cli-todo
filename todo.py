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

        if sys.argv[1] not in ["add", "done", "tasks"]:
            print("That's and invalid command\n")
            print("The available commands are:")
            print("\tadd - Adds a task. Prompts user for task text.")
            print("\tdone - Deletes a task. Prompts user for task id.")
            print("\ttasks - Displays all inputted tasks.")

            sys.exit()
        else:
            file = "todo.txt"
            lines = read_lines(file)
            # Note: If you change the separator you must change you TXT file is necessary to prevent problems
            separator = "±±±"
            match sys.argv[1]:
                case "add":
                    add(lines, separator)
                case "done":
                    done(lines, separator)
                case "tasks":
                    tasks(lines, separator)
                
def add(lines, separator):
    task = input("Task: ")

    if separator in task:
        sys.exit("Invalid task format. Try again")

    indexes = []
    if lines[0] != "0":
        indexes = get_indexes(lines, separator)
            
    with open("todo.txt", "w") as file:
        num_tasks = int(lines[0])

        file.write(str(num_tasks + 1) + "\n")

        if num_tasks == 0:
            file.write(f"1{separator}{task}\n")
        else:
            for line in lines[1:]:
                file.write(line + "\n")

            last_index = int(indexes.pop(len(indexes) - 1))
            file.write(str(last_index + 1) + separator + task + "\n")
        
        print(f"You have added the task: {task}")
        

def done(lines, separator):
    indexes = []
    if lines[0] == "0":
        sys.exit("You don't have tasks to do")
    else:
        id_task = input("Task to mark as done (ID): ")

        indexes = get_indexes(lines, separator)
    
    if id_task in indexes:
        with open("todo.txt", "w") as file:
            num_tasks = int(lines[0])

            file.write(str(num_tasks - 1) + "\n")
            
            for line in lines[1:]:
                if not line.startswith(id_task + separator):
                    file.write(line + "\n")
                else:
                    task = line.removeprefix(f"{id_task}{separator}")

            print(f"You have marked as done the task: {task}")
    else:
        sys.exit("Any task has that ID")

def tasks(lines, separator):
    if lines[0] == "0":
        sys.exit("You don't have tasks to do")
    else:
        print(f"You have {lines[0]} tasks to do:\n")

        for line in lines[1:]:
            num, task = line.split(separator)
            print(f"ID: {num} - {task}")

def read_lines(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    return lines

def get_indexes(lines, separator):
    indexes = []
    for line in lines[1:]:
            num, todo = line.split(separator)
            indexes.append(num)
    return indexes

if __name__ == "__main__":
    main()