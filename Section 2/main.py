user_prompt = 'Please enter a To-do: '

todos = []

while True:
    todo = input(user_prompt)
    todo = todo.capitalize()  # Capitalize the input before appending
    todos.append(todo)
    print(todos)
