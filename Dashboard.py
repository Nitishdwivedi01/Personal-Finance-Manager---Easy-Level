

*** Curently this file is not working properly there are some more modifications to be done. Once it is completed I will share the updated file or update this***


import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from data import data_last_n_entries
from Main_data import CSV 
CSV.add_entry(date, amount, expanse_type, category, description)
# CSV.check_duplicate_entry()
CSV.get_transection_summary(Start_date, End_date)
CSV.initialize_csv()

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
            

main()
