todos = []

while True:
    user_action = input("type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case 'edit':
            index = int(input("Enter the number of the item to be edited: ")) - 1
            todos[index] = input("Enter the new Todo: ")
        case "complete":
            todos.pop(int(input("Enter the number of the item completed: ")) - 1)
        case "exit":
            break
        case _:
            print("Invalid Command")

print("Bye!")