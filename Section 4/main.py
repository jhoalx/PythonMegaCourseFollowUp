todos = []

while True:
    user_action = input("type 'add', 'show', 'edit' or 'exit': ")
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo = input("Enter a todo: " )
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            index = int(input("Enter the number of the item to be edited: "))
            todos[index-1] = input("Enter the new Todo: ")
        case "exit":
            break
        case _:
            print("Invalid Command")


print("Bye!")