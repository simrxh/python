# Finance Tracker

A simple command-line Finance Tracker built with Python. It allows users to record income and expenses, view their current balance, view transaction history, and reset their financial data.

## Features

* Add income and expense transactions
* Calculate total income
* Calculate total expenses
* View current balance
* View all recorded transactions
* Reset all transaction data
* Automatically save data to a JSON file
* Store transaction date and time

## Technologies Used

* Python
* JSON
* `os` module
* `datetime` module

## How It Works

The program stores all transactions in a `finance_data.json` file.

Each transaction contains:

* Type — income or expense
* Amount
* Description
* Date and time

The balance is calculated using:

`Balance = Total Income - Total Expenses`

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-link>
```

2. Open the project folder:

```bash
cd finance-tracker
```

3. Run the Python program:

```bash
python finance_tracker.py
```

## Menu

```text
==== FINANCE TRACKER ====

1. Add Transaction
2. View Balance
3. View Transactions
4. Reset Data
5. Exit
```

## Example

```text
Enter a choice number: 1
Enter type(income/expense): income
Enter amount: 5000
Enter description: Salary

Transaction added successfully!

Enter a choice number: 2

------ FINANCE SUMMARY ------
Income: 5000
Expense: 0
Balance: 5000
-------------------------------
```

## Project Structure

```text
finance-tracker/
│
├── finance_tracker.py
├── finance_data.json
└── README.md
```

`finance_data.json` is created automatically when transactions are saved.

## Future Improvements

* Add transaction deletion
* Add categories for transactions
* Add monthly expense summaries
* Add a graphical user interface
* Add data visualization
* Add input validation and error handling

## Author

Simrah Ahmad
