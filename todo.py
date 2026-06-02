import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("You need to add a command")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        match sys.argv[1]:
            case "add":
                add()
            case "done":
                done()
            case "tasks":
                tasks()
            case "--help" | "-h":
                print("Help")
            case _:
                sys.exit("That's and invalid command")

def add():
    task = input("Task: ")
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
        else:
            for line in lines[1:]:
                file.write(line + "\n")

            last_index = int(indexes.pop(len(indexes) - 1))
            file.write(str(last_index + 1) + "±±±" + task + "\n")

def done():
    id_task = input("Task to mark as done (ID): ")
    indexes = []
    lines = []

    with open("todo.txt") as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    

    if lines[0] != "0":
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
        sys.exit("Any task has that ID")

def tasks():
    lines = []

    with open("todo.txt") as file:
        for line in file:
            lines.append(line.removesuffix("\n"))
    
    print(f"You have {lines[0]} tasks to do:")

    for line in lines[1:]:
        num, task = line.split("±±±")
        print(f"ID: {num} - {task}")

if __name__ == "__main__":
    main()