# Sofia Pereira Coutinho
# October 16, 2022

#This program will let the user simulate the financial status of a small diving and harvest operation


import random
import time


#define the operation function that determines the profit of each operation, according to their probabilities
def operation(harvest):
    """Calculates profit based on harvest type"""
    
    if harvest == "Lobster":
        percentage = random.randrange(1,101)
        if percentage < 11:
            profit = 125000
        elif percentage < 31:
            profit = -10000
        else:
            profit = 50000
        
    if harvest == "Bullwhip Kelp":
        percentage = random.randrange(1,101)
        if percentage < 41:
            profit = -10000
        else:
            profit = 45000
        
    if harvest == "Urchins":
        percentage = random.randrange(1,101)
        if percentage < 26:
            profit = -5000
        else:
            profit = 30000
    
    print("This year's focus:", harvest)
    print("Profit/loss for year " + str(year) + " is: $" + str(profit))
    
    #insert the profit value to the total profit list, to keep track of profit for each year
    total_profit.append(profit)

#define variable to ensure loop continuity until user wants to stop simulation
repeat = "yes"

#define list of harvest products in order
fish = ["Lobster", "Bullwhip Kelp", "Urchins", "Bullwhip Kelp"]



while "y" in repeat.lower():
    
    year = 1
    i = 0
    
    #define variables positive_years and total_profit for loop and if statement to run
    positive_years = "no"
    total_profit = []
    
    #3 conditions that must remain true for the simulation to continue
    while sum(total_profit) < 325000 and sum(total_profit) > -1 and "n" in positive_years:
        
        print("Year:", year)
                
        #i should be between 0 and 3
        if i == 4:
            i = 0
                    
        #run the operation function with the parameter harvest set to iterate along the list of fish (from 0 to 4)
        operation(fish[i])
                    
        #add one year
        year += 1
                
        #add onto the iterable variable
        i += 1
                 
        print("Total profit so far is: $" + str(sum(total_profit)) + "\n")
        time.sleep(1)
        
        if year > 5:
            
            #if all the profits in each of the last 5 years are positive, the simulation ends
            if total_profit[-5] >=0 and total_profit[-4] >= 0 and total_profit[-3] >= 0 and total_profit[-2] >= 0 and total_profit[-1] >= 0:
                positive_years = "yes"
        
    #print out the conditions that were satisfied for the simulation to end
    if sum(total_profit) < 0:
        print("Operations ended after", year - 1, "years due to negative total profit at year", year - 1)
        print("The total loss was: $" + str(sum(total_profit)))
        
    elif sum(total_profit) >= 325000:
        if positive_years == "no":
            print("Operations ended after", year - 1, "years due to total profit exceeding $325,000. You may now retire!")
        else:
            print("Operations ended after", year - 1, "years due to total profit exceeding $325,000; and 5 years of consecutive profit. You may now retire!")
        print("The total profit was: $" + str(sum(total_profit)))

    elif positive_years == "yes":
        print("Operations ended after", year - 1, "years due to 5 consecutive years of profit. You may now retire!")
        print("The total profit was: $" + str(sum(total_profit)))
    
            
    time.sleep(1)        
    repeat = input("\nWould you like to run another simulation? (yes/no) ")

print("Thank you for using our Diving & Oceaninc Harvesting Simulator!")