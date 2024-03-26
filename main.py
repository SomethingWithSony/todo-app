todos = []

while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  user_action = user_action.lower()

  match user_action:
    case "add":
      todo = input("Enter a todo: ") + "\n"
      file = open("data.txt", "r")
      todos = file.readlines()
      file.close()

      todos.append(todo)

      file = open("data.txt", "w")
      file.writelines(todos)
      file.close()

    case "show":
      file = open("data.txt", "r")
      todos = file.readlines()
      file.close()

      for index, item in enumerate(todos):
        print(f"{index + 1}: {item}")
    case "edit":
      todo_index = int(input("Number of the todo to edit: "))
      todo = input("Enter a todo: ")
      todos[todo_index - 1] = todo

      file = open("data.txt", "w")
      file.writelines(todos)
      file.close()

    case "complete":
      todo_index = int(input("Number of the todo to complete: "))
      todo = todos[todo_index -1]
      todos.pop(todo_index -1)

      file = open("data.txt", "w")
      file.writelines(todos)
      file.close()
      
      print(f"To-do : {todo} completed!")
    case "exit":
      break
    case _:
      print("An unknown command was entered!")