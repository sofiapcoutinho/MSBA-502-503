# Sofia Pereira Coutinho
# October 2, 2022


# This program will let a user analyze quadrants. Each quadrant has a certain number of galaxies, which have a certain number of planets. Each planet has an income amount.
# The program will ask for users' input, and provide them with relevant information regarding the quadrant.
# The user can analyze as many quadrants as desired



import time

print("Welcome to The Galaxy Analyzer!")
time.sleep(1)

#variable repeat will ensure the user can run the analysis on as many quadrants as desired
repeat = "yes"


#Start the loop for quadrant analysis. String manipulation functions ensure multiple variations of capitalization and spacing are captured.
while repeat.lower().strip() == "yes":

    #defining all relevant variables by setting them to 0
    cnt_planets = 0
    qdr_income = 0
    
    dist20 = 0
    dist40 = 0
    dist60 = 0
    dist80 = 0
    dist_plus = 0
    
    #user must input how many galaxies to analyze in this quadrant
    galaxies = int(input("How many galaxies would you like to analyze? "))
    
    #starts the loop to analyze each galaxy
    for i in range(1, galaxies +1,1):
        
        planets = int(input("How many planets are in Galaxy" + str(i) + "? "))
        
        #cnt_planets variable will keep track of how many planets are in the quadrant
        cnt_planets += planets
        
        #defines gxy_income variable and resets it to 0. tracks the total income for galaxy i
        gxy_income = 0
        
        #start the loop to analyze planets' income
        for j in range(1,planets +1,1):
            income = int(input("What was Planet" + str(j) + "'s income last year (in trillions)? "))
            
            #adds the income amount for planet j to the total galaxy i income
            gxy_income += income
            
            #adds the income amount for planet j to the total quadrant income
            qdr_income += income

        #keeps track of the distribution of the quadrant's income by galaxy. Adds 1 to the appropriate variable, depending on each galaxy's income.
        if gxy_income < 20000:
            dist20 += 1
        elif gxy_income < 40000:
            dist40 += 1
        elif gxy_income < 60000:
            dist60 += 1
        elif gxy_income < 80000:
            dist80 += 1
        else:
            dist_plus += 1
                
    print()
    time.sleep(1)
    
    #The fFollowing print statements indicate relevant information and summary statistics to the user
    
    print("Number of planets in this quadrant:", cnt_planets)
    print("Number of planets per galaxy:", cnt_planets/galaxies)
    
    print()
    time.sleep(1)
    
    print("Average planetary income = $" + str(round(qdr_income/cnt_planets,2)) + " trillions")
    print("Average galactic income = $" + str(round(qdr_income/galaxies,2)) + " trillions")
    
    print()
    time.sleep(1)
    
    print("Income distribution:")
    print("Less than $20,000:", dist20, "galaxy(s)")
    print("At least $20,000 and less than $40,000:", dist40, "galaxy(s)")  
    print("At least $40,000 and less than $60,000:", dist60, "galaxy(s)")
    print("At least $60,000 and less than $80,000:", dist80, "galaxy(s)")
    print("At least $80,000:", dist_plus, "galaxy(s)")
    
    print()
    time.sleep(1)
    
    #User must answer 'yes' for the program to loop back and analyze another quadrant. If not, the while loop will end.
    repeat = input("Would you like to analyze another quadrant? (yes/no) ")

print("Thank you for using The Galaxy Analyzer!")