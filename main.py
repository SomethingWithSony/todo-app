while True:

  # Get user input, lowercase  and removes space characters 
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  user_action = user_action.lower()

  match user_action:
    case "add":
      todo = input("Enter a todo: ") + "\n"

      with open("data.txt", "r") as file:
        todos = file.readlines()
      
      todos.append(todo)

      with open("data.txt", "w") as file:
        file.writelines(todos)
      

    case "show":
      with open("data.txt", "r") as file:
        todos = file.readlines()

      new_todos = [item.strip("\n") for item in todos]
      for index, item in enumerate(new_todos):
        print(f"{index + 1}: {item}")


    case "edit":
      todo_index = int(input("Number of the todo to edit: "))
      index = todo_index -1
      todo = input("Enter a todo: ")
      todos[index] = todo

      with open("data.txt", "w") as file:
        file.writelines(todos)

    case "complete":
      todo_index = int(input("Number of the todo to complete: "))
      index = todo_index -1
      todo = todos[index]
      todos.pop(index)

      with open("data.txt", "w") as file:
        file.writelines(todos)

      print(f"To-do : {todo} completed!")
    case "exit":
      break
    case _:
      print("An unknown command was entered!")