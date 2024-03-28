def get_todos():
  with open("data.txt", "r") as file:
    todos = file.readlines()
  return todos 


def write_todos():
  with open("data.txt", "w") as file:
      file.writelines(todos)


while True:

  # Get user input, lowercase  and removes space characters 
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  user_action = user_action.lower()

  
  if "add" in user_action:
    
    todo = user_action[4:]
    todo = todo.strip(" ")
    if len(todo) == 0:
      todo = input("Enter a todo: ") + "\n"
    
    todo += "\n"
    todos = get_todos()
    
    todos.append(todo)
    write_todos()
    
  elif "show" in user_action:
    todos = get_todos()
    new_todos = [item.strip("\n") for item in todos]
    for index, item in enumerate(new_todos):
      print(f"{index + 1}: {item}")
      
  elif "edit" in user_action:
    try:
      todo_index = user_action[5:]
      todo_index = todo_index.strip(" ")
      
      if len(todo_index) == 0:
        todo_index = int(input("Number of the todo to edit: "))
      todo_index = int(todo_index)
      

      index = todo_index -1
      todo = input("Enter a todo: ")
      
      todos = get_todos()
    
      todos[index] = todo + "\n"
      write_todos()
    except ValueError:
      print("Invalid command!")
      continue
    except IndexError:
      print("There is no item with that number!")
      
  elif "complete" in user_action:
    try:
      todo_index = user_action[9:]
      todo_index = todo_index.strip(" ")
      
      if len(todo_index) == 0:
        todo_index = int(input("Number of the todo to complete: "))
      todo_index = int(todo_index)
      index = todo_index -1
      
      todos = get_todos()
        
      todo = todos[index]
      todos.pop(index)
      write_todos()
      print(f"To-do : {todo} completed!")
    except ValueError:
      print("Invalid command!")
      continue
    except IndexError:
      print("There is no item with that number!")
      continue
  
  elif "exit" in user_action:
    break
  else:
    print("Unkown command ")

print("Bye bye!")