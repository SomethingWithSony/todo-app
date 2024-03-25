todos = []

while True:
  user_action = input("Type add, show, edit or exit: ")
  user_action = user_action.strip()
  user_action = user_action.lower()

  match user_action:
    case "add":
      todo = input("Enter a todo: ")
      
      todos.append(todo)
    case "show":
      for index, item in enumerate(todos):
        print(f"{index + 1}: {item}")
    case "edit":

      todo_index = int(input("Number of the todo to edit: "))
      todo = input("Enter a todo: ")
      todos[todo_index - 1] = todo
    case "exit":
      break
    case _:
      print("An unknown command was entered!")