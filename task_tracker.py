# THE SINGLE ELEMENT CLASS
class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False  # Default value when a task is created

    def mark_as_completed(self):
        self.is_completed = True 
        

    def mark_as_incompleted(self):
        self.is_completed = False
        


# THE CONTROLLER CLASS (THE CONTAINER)
class TaskManager:
    def __init__(self):
        self.tasks_list = []  # The array (list) that will hold the Task objects

    def add_task(self, title):  # The function that will add a task to the list
      for task in self.tasks_list:
        if task.title == title: # Check if the task already exists in the list
            print("***ERROR*** Task already exists")
            return  

      self.tasks_list.append(Task(title)) 
      print("Task added successfully!")
      

    def view_tasks(self): # The function that will display all tasks in the list
        if not self.tasks_list:  # Check if the task list is empty
           print("\nYour task list is empty!")
           return

        print("\nYour task list:")
        for index, task in enumerate(self.tasks_list):
          if task.is_completed:
            print(f"\t{index + 1}) [X] {task.title}")
          else:
            print(f"\t{index + 1}) [ ] {task.title}")
  

    def complete_task(self, user_index): # The function that will mark a task as completed
      task_index = user_index - 1  

      if 0 <= task_index < len(self.tasks_list): # Check if the task index is valid
        if self.tasks_list[task_index].is_completed == True:
            print("Task already completed")
        else:
            self.tasks_list[task_index].mark_as_completed()
            print("Task marked as completed!")
      else:
        print("***ERROR*** Invalid task index")
      

    def incomplete_task(self, user_index): # The function that will mark a task as incomplete
      task_index = user_index - 1

      if 0 <= task_index < len(self.tasks_list): # Check if the task index is valid
        if self.tasks_list[task_index].is_completed == False:
            print("Task is already incomplete")
        else:
            self.tasks_list[task_index].mark_as_incomplete() 
            print("Task marked as incomplete!")
      else:
         print("***ERROR*** Invalid task index")
      

manager = TaskManager()

# THE USER INTERFACE
while True:
    print("\n--------------------------------------------------------------------------")
    print("PRESS 1 TO ADD A TASK")
    print("PRESS 2 TO VIEW ALL TASKS")
    print("PRESS 3 TO MARK A TASK AS COMPLETE")
    print("PRESS 4 TO MARK A TASK AS INCOMPLETE")
    print("PRESS 5 TO EXIT")

    # Input conversion to integer for menu selection
    choice = int(input("\nWhat would you like to do? "))

    # Input validation for the main menu
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
      print("\n***ERROR*** Invalid choice, please try again.")
      continue


    # OPTION 1: ADD A TASK
    if choice == 1:
      title = str(input("\nWhat task would you like to add? ")).title()
      manager.add_task(title)

    # OPTION 2: VIEW ALL TASKS
    if choice == 2:
      manager.view_tasks()

    # OPTION 3: MARK A TASK AS COMPLETE
    if choice == 3:
      manager.complete_task(int(input("\nWhich task would you like to mark as complete? ")))

    # OPTION 4: MARK A TASK AS INCOMPLETE
    if choice == 4:
      manager.incomplete_task(int(input("\nWhich task would you like to mark as incomplete? ")))

    # OPTION 5: EXIT 
    if choice == 5:
      print("\nGoodbye!!")
      break
