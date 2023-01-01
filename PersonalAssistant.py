class PersonalAssistant:
  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There is no contact with that name"

  def get_contacts(self):
    return self.contacts   

  def add_contact(self, name, title):
    if name in self.contacts:
      return f"You already have a contact named {name}."
    else:
      self.contacts[name] = title
      return f"{name} has been added to contacts."

  def remove_contact(self, name):
    if name in self.contacts:
       self.contacts.pop(name)
       return f"{name}'s contact has been removed."
    else:
       return "Sorry, there is no contact for that person."

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
        return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
        return "Birthday not found."

  def add_birthday(self, name, date):
      if name in self.birthdays:
          return f"You already have a birthday for {name}"
      else:
          self.birthdays[name] = date
          return f"{name}'s birthday has been added."

  def remove_birthday(self, name):
    if name in self.birthdays:
       self.birthdays.pop(name)
       return f"{name}'s birthday has been removed."
    else:
       return "Sorry, there is no recorded birthday for that person."