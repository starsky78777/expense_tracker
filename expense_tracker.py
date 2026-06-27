# ----- We import tools  that python already has built-in -----
import csv                      # help us read and write .cvs files
import os                       # help us check if file exists
from datetime import datetime   # give us today's date automatically 

# ----- The name of the file where all expenses will be save -----
FILE = "expenses.csv"

# ----- A list of spending categories the user can choose from -----
CATEGORIES = [
    "Food", "Transport", "Bills", 
    "Health", "Education", "Other"
]

#   ------------------------------------------------------
#   FUNCTION 1 - Add a new expense
#   ------------------------------------------------------
def add():
    print("\n-- ADD EXPENSE --")

    #Get today's date automatically, frormated as YYYY-MM-DD
    date = datetime.now().strftime("%Y-%m-%D")

    #Ask the user to type the amount they spent
    amount = input("Amount: ")

    #Show the category list with numbers so user can pick one
    for i, c in enumerate(CATEGORIES, 1): #enumerate adds 1,2,3... to the list
        print(f"  [{i}] {c}")
    
    #Subtract 1 because lists start at index 0, but we showed numbers from 1
    choice      = int(input("Category [1-6]: ")) - 1
    category    = CATEGORIES[choice] #pick the matching category from the list

    # Ask a short description of the expense
    desc    = input("Description: ")

    # Check if the file arleady exist on disk
    file_exists = os.path.exists(FILE)

    # Open the file in APPPEND mode ("a") so we never overwrite old data
    with open(FILE, "a", newline="") as f:
        writer  = csv.writer(f)

        #If the file is brand new, write the header row first
        if not file_exists:
            writer.writerow(["date", "amount", "category", "description"])
        
        #Write the actual expense as one new row
        writer.writerow([date, amount, category, desc])

    print("Saved!") #confirm to the user that it worked


# ----------------------------------------------------------------------
#   FUNCTION 2 - View all saved expense
# ----------------------------------------------------------------------
def view():
    print("\n-- ALL EXPENSES --")

    #If the file doesn't exist yet, there's nothing to show
    if not os.path.exists(FILE):
        print("No expenses yet")
        return #exit the function early
    
    #Open the file in the READ mode ("r") abd print every line
    with open(FILE, "r") as f:
        for line in f:
            print(line.strip()) # .strip() is to removes the invisible \n at line ends


# ---------------------------------------------------------------------
#   FUNCTION 3 - Main menu loop
# ---------------------------------------------------------------------
def main():
    # "while True" runs forever until the user choose to quit
    while True:
        print("\n[1] Add   [2] View   [3] Quit")
        choice = input("Choose: ")

        if      choice == "1": add()    #run the add function
        elif    choice == "2": view()   #run the view function
        elif    choice == "3": break    #break, exits the while loop --> program ends




# --- This line starts the program ---
# It means: only run main() if this file is run directly
# (not if another script imports it)
main()




