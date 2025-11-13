# Tyrone Chen

# Date: 24/10/2025 

on = True
while(on):
    try:
        width = float(input("Please tell me the width of the fence that is bigger than 0:  ")) #Asks user for the width
        length = float(input("Please tell me the length of the fence that is bigger than 0: ")) #Asks user for the length
    
        if(width and length > 0): #Checks if the width and length is bigger than 0
            print("Area is",width*length) #Prints area
            print("Perimeter is",(width*2)+(length*2)) #Prints perimeter

            switch = input("Go again? (enter to restart): ") #Asks user if they want to run the code again
            if(switch == ""): #Checks the response
                on = True #Runs the code again
            else:
                on = False #Stops the code
        else:
            print("Please enter a number bigger than 0!") #The user has submited a number equal or less than 0

    except ValueError:
        print("This is not a valid number!") #The user has not submitted a valid number to calculate
    
    
