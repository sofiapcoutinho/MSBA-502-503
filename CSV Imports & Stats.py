#Sofia Pereira Coutinho
#November 9, 2022

#This program assists the business "Adrek Robotics" in tracking its financial transactions.
#This program maintains up-to-date records on transaction data and allows the user to both load new transaction data and analyze existing transaction data.


import csv, os.path

print("Welcome to the Adrek Robotics transaction tracker!")

#variable to ensure as many actions as user wants
repeat = "yes"

while "y" in repeat.lower().strip():
    
    #user input which action they want to perform
    action = input("\nWhat action would you like to do? (import/statistics) ")
    count = 0
    
    #check if transactions ledger file exitst yet. If not, create it
    if os.path.isfile("transaction_ledger.csv") == False:
        with open("transaction_ledger.csv", "wb") as file:
            pass
        
    #program to run if user wants to import a file
    if "imp" in action.lower().strip():
        file_name = input("\nWhat file would you like to import? ")
        
        #add csv extension, in case user has not already
        if file_name[-4:] != ".csv":
            file_name += ".csv"
            
        #save the user's file contents in a variable
        with open(file_name, "r") as user_file:
            user_file_contents = csv.reader(user_file)
                
            try:           
                #store transactions file content in a variable        
                with open("transaction_ledger.csv", "r") as file_read:
                    file_contents = csv.reader(file_read)
                        
                    #store IDs already in transactions file in a list
                    ledger_ids = []
                    for row in file_contents:
                        ledger_ids.append(row[0])
                        
                    #check each ID in user's file if they match any item in the existing transactions file. Append user's transaction in transaction file if not
                    for line in user_file_contents:
                        ID = line[0]
                                
                        if ID in ledger_ids:
                            print("Data for ID", ID, "is already in transaction records.")
                        else:
                            with open("transaction_ledger.csv", "a") as file_append:
                                writer = csv.writer(file_append, lineterminator = "\n")
                                writer.writerow(line)
                                count += 1
                    
                print("\n" + str(count) + " new transactions recorded.")
                        
            except:
                print("\nI'm sorry, that file is not valid. Please try again.")           
        
    #program to run if user wants statistics            
    elif "stat" in action.lower().strip():

        with open("transaction_ledger.csv", "r") as file_read:
            file_contents = csv.reader(file_read)
            total_amount = 0
                
            #loop through transactions file to count rows and amount pending
            for line in file_contents:
                count += 1
                amount = float(line[3])
                status = line[4]
                if status.lower().strip() == "pending":
                    total_amount += amount
            
            #print how many transactions have been recorded, and the dollar amount pending
            if count > 0:
                print("\nNumber of current transactions:", count)
                print("Total $ amount pending:", round(total_amount,2))
                
            else:
                print("\nNo transactions recorded yet.")
                
    else:
        print("Sorry, that operation is not supported. Please try again.")
        
    repeat = input("\nWould you like to run other analyses? (yes/no) ")


print("\nProgram ended.")