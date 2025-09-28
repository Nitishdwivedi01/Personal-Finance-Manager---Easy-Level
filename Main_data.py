import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from data import get_amount, get_category,get_date, get_description, get_expanse_type,data_last_n_entries
def read_file():
    try:
        df = pd.read_csv("Finance_data.csv")
        # print("Data loaded successfully.\n")
    except FileNotFoundError:
        print("Finance_data.csv file not found. Please ensure the file exists.")
        
    
df = pd.DataFrame(columns=["Date", "Amount", "Expanse_Type", "Category", "Description"])
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors='coerce')

class CSV:
    CSV_file = "Fincance_data.csv"
    Field_names = ["Date", "Amount", "Expanse_Type", "Category", "Description"]
    global df
    
    @classmethod
    def initialize_csv(cls):
        try:
            cls.CSV_file = "Finance_data.csv"
            with open(cls.CSV_file, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Amount", "Expanse_Type", "Category", "Description"]) # Header row
                
        except FileNotFoundError:
            print("File not found. Creating a new file.")
       
        except FileExistsError:
            return [f"File {cls.CSV_file} already exists."]

        return [f"File {cls.CSV_file} initialized successfully."]
    
    
    @classmethod
    def add_entry(cls, date, amount, expanse_type, category, description):
        with open(cls.CSV_file, 'a', newline='') as file: # With is also called context manager, it close file once code processing is over and also prenvent memory leak.
            writer = csv.writer(file) 
            # writer = csv.DictWriter(file, fieldnames= cls.Field_names) # we can aslo give fieldnames = cls.Field_names to remove the below line of code.
        #     writer.writerow({
        #     "Date": date,
        #     "Amount": amount,
        #     "Expanse_Type": expanse_type,
        #     "Category": category,
        #     "Description": description
        # })
            writer.writerow([date, amount, expanse_type, category, description])
        return ["Entry added successfully."]
    
    
    
    @classmethod
    def check_duplicate_entry(cls, Date, Amount, Expanse_Type, Category, Description):
        with open(cls.CSV_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (row["Date"] == Date and
                    float(row["Amount"]) == Amount and
                    row["Expanse_Type"] == Expanse_Type and
                    row["Category"] == Category and
                    row["Description"] == Description):
                    return True
        return False
    
    @classmethod
    
    def get_transection_summary(cls, Start_date, End_date):
        df = pd.read_csv(cls.CSV_file, parse_dates=["Date"], dayfirst=True)
        df["Date"]= pd.to_datetime(df["Date"], dayfirst = True )
        
        Start_date_str = input("Enter the start date (DD-MM-YYYY):- ")
        End_date_str = input("Enter the End date (DD-MM-YYYY):- ")
        
        Start_date = datetime.strptime(Start_date_str, "%d-%m-%Y").date()
        End_date = datetime.strptime(End_date_str, "%d-%m-%Y").date()
        
        if Start_date:
            df = df[df["Date"] >= pd.to_datetime(Start_date)]
        
        if End_date:
            df = df[df["Date"] <= pd.to_datetime(End_date)]
            
        mask = (df["Date"] >= Start_date) & (df["Date"] <= End_date)
        Filtered_data = df.loc[mask]
        
        if Filtered_data.empty:
            print("No data found for the given filters.")
        else:
            print("\n Filtered data based on the given filters:- \n")
            print(Filtered_data)
            
        print("\n Generating summary report for the given range of filter...\n")
        total_income = Filtered_data[Filtered_data["Expanse_Type"].str.lower() == "Income"]["Amount"].sum().round(2)
        total_expanse = Filtered_data[Filtered_data["Expanse_Type"].str.lower() == "Expense"]["Amount"].sum().round(2)
        profit_loss = total_income - total_expanse
        print(f"\n Total Income: ${total_income}")
        print(f" Total Expense: ${total_expanse}")  
        print(f" Profit/Loss: ${profit_loss}\n")
        
        return Filtered_data


def add_entry():
    CSV.initialize_csv()
    print("Please provide the following details to add a new entry:- \n")
    
    Date = get_date("Enter the date (DD-MM-YYYY) or press Enter for today's date: ", allow_default=True)
    Amount = get_amount()
    Expanse_Type = get_expanse_type()
    Category = get_category()
    Description = get_description()
    print("\n Entry added successfully.") 

    if CSV.check_duplicate_entry(Date, Amount, Expanse_Type, Category, Description):
        print("Duplicate entry detected. Entry not added.")
        return ["Duplicate entry detected. Entry not added."]
        
    return CSV.add_entry(Date, Amount, Expanse_Type, Category, Description)

def main():
    CSV.initialize_csv()
    while True:
        
        print("\nWelcome to Personal finance Manager, Let's start to manage your expanses")
        print("     1- To add new transection.")
        print("     2- To view transection.")
        print("     3- To delete transecton.")
        print("     4- To View summary.")
        print("     5- To end operation.\n")
        
        choice = int(input("\nEnter you choice (only numbers):- "))
        
        if choice == 1:
            CSV.add_entry()
            print("\nChecking for duplicate data if already in database")
            if CSV.check_duplicate_entry == True:
                print("Duplicate Entry")
            else:
                pass
            print("\nEntry added succesfully")
            print("\nIf you want to add more entry give Y or N to back to main manu.")
            
            user = input("Please enter your remark: ").strip().upper()
            if user == "Y":
                CSV.add_entry()
                print("\nChecking for duplicate data if already in database")
                if CSV.check_duplicate_entry == True:
                    print("Duplicate Entry")
                else:
                    pass
                print("\nEntry added succesfully")
            elif user == "N":
                main()
                print("Returning to main manu")
            else:
                print("Please enter the correct remark")
                continue
                
        elif choice == 2:
            print("\n   1- To view transection with start date and end date")
            print("\n   2- To view transetion of last N days \n we can also filter the data based on expanse types")
            print("\n   0- To return to main manu")
            
            input1= int(input("Enter your choice (1-2 or 0):- "))
            if input1 == 1:
                Start_date_str = input("Enter the start date (DD-MM-YYYY):- ")
                End_date_str = input("Enter the End date (DD-MM-YYYY):- ")\
                # Both the input will give string as output so change to datetime formate
                Start_date = datetime.strptime(Start_date_str, "%d-%m-%Y").date()
                End_date = datetime.strptime(End_date_str, "%d-%m-%Y").date()
                
                CSV.get_transection_summary(Start_date,End_date)
                print(f"To total transection and summary form {CSV.Start_date} to {CSV.End_date} is:- ")
            elif input1 == 2:
                print("Data of last N days:- ")
                data_last_n_entries()
            elif input1 == 0:
                main()
            else:
                print("Please enter the valid number:- ")
                
        elif choice == 3:
            pass
            print("Sorry!!! This option is curently not active. Returning to main manu.\n")
            main()
        
        elif choice == 4:
            pass  
            print("Sorry!!! This option is curently not active. Returning to main manu.\n")
            main()       
        
        elif choice == 5:
            pass 
            print("Closing this operation.\n")
            main()
        
        else:
            print("Please enter the valid number 1-5:- ")
            

            
if __name__ == main:
    main()  