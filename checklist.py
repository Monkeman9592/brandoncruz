
'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
import numbers
from operator import index


checklist = []

print(checklist)

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    print(checklist)
     

def update(index, item):
    checklist.extend(index)
     

def destroy(index):
    checklist.remove(index)
     

#def mark_completed(index):
  #  checklist.insert(index)

#def list_all_items():
     # List all items code here

#def user_input(prompt):
     # Get user input here

def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)
        running = True

        return running

    if function_code == "M":
        input_item = input("what would you like to mark off")
        mark_completed(input_item)
        running = True

        return running

    if function_code == "D":
        input_item = input("what would you like deleted ")
        destroy(input_item)
        running = True

        return running

    if function_code == "R":
         read(index)
         running = True

         return running
    
    if function_code == "Q":        
        running = False

        return running

    

running = True

while running:
    selection =input("Press C to add to list, R to Read from list, P to display list, Q to quit , M to mark completed, And D to destroy: ").upper()
    running = select(selection)