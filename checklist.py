'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist

from operator import index
checklist = []
print(checklist)
# Define Functions
def create(item):
    checklist.append(item)

def read(index):
      print(checklist[index])
     
def update(index, item):
    checklist[index] = item
     
def destroy(index):
    checklist.pop(index)
     
def mark_completed(index):
    '''
    What we are doing is just trying to "check off" an item that already exist in our list]
    ex) if our list is ["eat veggies", "workout", "sleep"] then we want the result of the mark function to look like ["eat veggies", "* workout", "sleep"]

    "eat veggies" if index = 0
    'eat veggies" = "* eat veggies"
    '''
    checklist[index] = "* " + checklist[index]

def list_all_items():

    for item in checklist:
        print(item)
    
def select(function_code):
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)
        running = True

        return running
    elif function_code == "R":
        '''
        When using input( ) you can only return a string data type, python has four built in functions that help with dealing with different data types and type conversions: type( ) tells you the current type of a data entry, int( ) can change a data type to an integer, str( ) can change a data type to a string and dict( ) / list( ) can change things to a dictionary or list respectively
        '''
        input_item = input("what index element would you like to read ")
        read(int(input_item))
        
        running = True


    elif function_code == "U":
        input_index = input("waht index would you like to call  ")
        input_item = input("what item would you like to update in index ")    
        update (int(input_index), input_item)
        running = True
        return running

    elif function_code == "D":
        input_item = input("what would you like deleted ")
        destroy(int(input_index))
        running = True
        return running

    elif function_code == "M":
        input_item = input("what would you like to mark off  ")
        mark_completed(int(input_item))
        running = True

        return running

    elif function_code == "L":
        list_all_items()
        running = True

        return running

    elif function_code == "Q":   
        print("you have quit")     
        running = False

        return running

running = True

while running:
    selection =input("Press C to add to list, R to Read from list, L to display list, Q to quit , M to mark completed, U to update,  And D to destroy: ").upper()
    running = select(selection)