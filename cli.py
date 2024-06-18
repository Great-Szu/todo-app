from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or complete (type exit to exit):")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todo = todo.title() + '\n'

        todos = get_todos()

        todos.append(todo)

        # We read file and put all the lines to the variable todos, then
        # we append this variable with next input and rewrite the file with this variable
        # Now we use function to do this
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # This for loop automatically creates spaces (\n) between outputs. In this
        # case we are removing the extra space (added in case add) to produce clean code
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            todo_to_edit = todos[number]
            new_todo = input(f"What to put instead of {todo_to_edit.strip("\n")}?:")
            todos[number] = new_todo.title() + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos(todos)

            print(f"Congrats! You have just completed {todo_to_remove.strip()}")

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")


print("Bye!")