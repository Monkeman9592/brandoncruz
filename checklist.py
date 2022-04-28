
'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
import numbers


checklist = []

print(checklist)

# Define Functions
def create(item):
    checklist.append(item)

# def read(index):
#     # Read code here

# def update(index, item):
#     # Update code here

# def destroy(index):
#     # Destroy code here

# def mark_completed(index):
#     # Add code here that marks an item as completed

# def list_all_items():
#     # List all items code here

# def user_input(prompt):
#     # Get user input here

def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)
        running = True

        return running

    # if function_code == "R":
    #     input_item = input("Input item index: ")
    #     read(input_item)
    #     running = True

    #     return running
    
    if function_code == "Q":        
        running = False

        return running

    

running = True

while running:
    selection =input("Press C to add to list, R to Read from list, P to display list, and Q to quit: ").upper()
    running = select(selection)