import streamlit as st

st.title("To-Do List")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def view_task(self, task):
        return task
    
    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task    

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

todo_list = ToDoList()

# Input for ny opgave
new_task = st.text_input("Enter a new task")

#Knap til at tilføje opgave
if st.button("Add Task"):
    if new_task:
        todo_list.create_task(new_task)

# Visning af opgaver
st.write("Your tasks:")
for task in todo_list.tasks:
    st.write(task)

if todo_list.tasks:
    view_task = st.selectbox("Select a task to view", todo_list.tasks)
    if st.button("View Task"):
        viewed_task = todo_list.view_task(view_task)
        if viewed_task:
            st.write(f"Viewing Task: {viewed_task}")
        else:
            st.write("Task not found")

# st.help(st.)