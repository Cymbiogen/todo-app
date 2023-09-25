from functions import write_todos, get_todos
import time

user_prompt = "Type add, show, edit, complete or exit: "
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):

        # file = open("files/todos.txt", 'r')
        # todos = file.readlines()
        # file.close()
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        #            new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            number = int(user_action[9:])
            todos.pop(number - 1)

            write_todos(todos)

        except IndexError:
            print("There is no todo with that value")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command not valid")
print("bye")
