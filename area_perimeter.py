# Tyrone Chen

# Date: 24/10/2025 

on = True
while(on):
    try:
        width = float(input("Please tell me the width of the fence that is bigger than 0:  "))
        length = float(input("Please tell me the length of the fence that is bigger than 0: "))
        
        print("Area is",width*length)
        print("Perimeter is",(width*2)+(length*2))

        switch = input("Go again? (enter to restart): ")
        if(switch == ""):
            on = True
        else:
            on = False
        
    except ValueError:
        print("This is not a valid number!")
