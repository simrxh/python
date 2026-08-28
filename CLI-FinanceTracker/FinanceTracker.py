import json
import os  #checks if file exists 
from  datetime import datetime

DATA_FILE = "finance_data.json"


# LOAD FUNCTION 
def load_data():
    # check if file exists
    if not os.path.exists(DATA_FILE):
        return{"transactions": []}
    
    with open(DATA_FILE, 'r') as json_file:
        return json.load(json_file)


# SAVE DATA 
def save_data(data):
    with open(DATA_FILE,"w") as json_file:
        json.dump(data, json_file)


# ADD TRANSACTION 
def add_transaction(data):
    t_type = input("Enter type(income/expense) : ")
    amount = float(input("Enter amount: "))
    description =input("Enter description: ")
    
    
    transaction = {
        "type":t_type,
        "amount":amount,
        "description":description,
        "date":str(datetime.now())
    }
    
    data["transactions"].append(transaction)
    
    save_data(data)
    
    print("Transaction added succesfully!")


# VIEW BALANCE 
def view_balance(data):
    income = 0
    expense = 0
    
    for t in data["transactions"]:
        if t["type"] == "income":
            
            income += t["amount"]
            
        elif t["type"] == "expense":
            
            expense += t["amount"]
            
    balance = income - expense
    
    print("\n------ FINANCE SUMMARY ------")   
    print(f"Income: {income}") 
    print(f"Expense: {expense}") 
    print(f"Balance: {balance}") 
    print("-------------------------------\n") 
    
    
# VIEW TRANSACTIONS 
def view_transactions(data):
    if not data["transactions"]:
        print("No transaction found.")
        return
    for i , t in enumerate(data["transactions"]):
        print(f"{i}.[{t['type'].upper()}] {t['amount']}- {t['description']} {t['date']}")


# DELETE TRANSACTIONS
def reset_data(data):
    confirm = input("Are you sure you want to reset the data? (yes/no): ")
    
    if confirm == "yes":
        data["transactions"] = []
        save_data(data)
        print("All data reset successfully.")
    else:
        print("Reset Cancelled")
        
# main function 
def main(): 
     data = load_data()
    
     while True:
         
        # display menu    
         print("\n ==== FIANANCE TRACKER ====")
         print("1. Add Transaction")
         print("2. View Balance")
         print("3. View Transactions")
         print("4. Reset Data")
         print("5. Exit")
         
         choice = int(input("Enter a choice number: "))
         
         if choice == 1:
             add_transaction(data)
         elif choice == 2:
             view_balance(data)
         elif choice == 3:    
            view_transactions(data)
         elif choice == 4:    
            reset_data(data)
         elif choice == 5:
            print("Exiting the tracker")
            break
         else :
            print ("Invalid Choice")
            
if __name__ == "__main__":
    main()
