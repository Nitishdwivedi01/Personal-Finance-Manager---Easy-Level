# Personal-Finance-Manager---Easy-Level
A simple Python-based Personal Finance Tracker that helps you record, filter, and analyze your daily expenses and income. This project is currently at an easy level, but more advanced features will be added in the upcoming days.

Finance file contains the synthetic data made by AI, If you upload data using code it will also be stored in the same file.

This project is designed to track personal financial transactions with a focus on learning and practicing:

File handling with CSV.
Date parsing and filtering transactions by date range.
Handling Income & Expense categories with subcategories.
Avoiding duplicate entries.
Summarizing data to calculate total income, total expenses, and profit/loss.
The project is modular, allowing you to expand functionality into advanced levels (dashboards, visualizations, database integration, etc.).

⚡ Features Implemented (Easy Level)

✅ Add new transactions (Date, Amount, Type, Category, Description).
✅ Categorize expenses into 15 predefined categories (with subcategories).
✅ Automatically handle duplicate entries.
✅ Filter transactions by date range, type, and category.
✅ Generate a summary report showing:
-Total Income
-Total Expense
-Profit/Loss
✅ Store all data in a CSV file (Finance_data.csv) for persistence.

🚀 Future Enhancements (Advanced Level)

🔹 Advanced data visualization using Matplotlib/Seaborn/NumPy.
🔹 Export summary reports in PDF/Excel formats.
🔹 Integration with a database (MySQL Server).
🔹 Create a Dashboard Menu / GUI Interface for better usability.
🔹 Machine learning module to analyze spending patterns.
🔹 Cloud sync and multi-user support.
🔹 Store data in the user DB and create a Desktop application using Tkinter library .

🛠️ Technologies Used

Python 3.x
pandas (for data handling & filtering)
CSV module (file storage)
datetime (date parsing & filtering)

▶️ How to Run
Clone the repository or download files and same all in one folder
Install dependencies (if not already installed)
Run the project:- python Main_data.py

Example Usage
Enter the date (DD-MM-YYYY) or press Enter for today's date: 26-09-2025  
Enter amount: 1500  
Enter the expense type (I/Income or E/Expense): E  
Please define the category of the expense: Water  
Enter a short description: Paid water bill  

⭐ Contributions are welcome! Future advanced versions will need:

Better UI
Database integration
Visualization modules
Feel free to fork the repo and create a pull request
