# Tyrone Chen
# 7/11/2025

on = True
while(on):

    try:
        sec = float(input("Please give me the seconds: "))
        mm = float(input("Please give me the mm: "))
        gram = float(input("Please give me the grams: "))
        vol = float(input("Please give me the volume: "))

        try:
            choice = input("Which one do you want to convert? (sec/mm/gram/vol): ").lower()
            if (choice == "sec"):
                print("Seconds converted is",sec//3600,"hours")
            elif (choice == "mm"):
                print("mm converted is",mm//1000,"metres")
            elif (choice == "gram"):
                print("grams converted is",gram//1000,"kgs")
            elif (choice == "vol"):
                print("mLitres converted is",vol//1000,"Litres")
        except:
            print("Invalid choice!")
            
    except:
        print("Invalid number!")
    
    finally:
        switch = input("Go again? (enter to restart): ")
        if(switch == ""):
            on = True
        else:
            on = False