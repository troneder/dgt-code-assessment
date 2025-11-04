# Tyrone Chen

# Date: 24/10/2025 

on = True
while(on):
    width = (input("Please tell me the width of the fence that is bigger than 0:  "))
    length = (input("Please tell me the length of the fence that is bigger than 0: "))

    if(width.isnumeric() and length.isnumeric()):
        if(float(width) and float(length) > 0):
            width = float(width)
            length = float(length)

            print("Area is",width*length)
            print("Perimeter is",(width*2)+(length*2))
            
            switch = input("Go again? (enter to restart): ")
            if(switch == ""):
                on = True
            else:
                on = False
        else:
            print("Please enter a number bigger than 0!")    
    else:
        print("This is not a valid number!")