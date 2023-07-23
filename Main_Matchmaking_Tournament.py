# #IMPORT LIBRARIES
import time
import Double_Round_Robin
import Single_Elimination

# #MAIN SCREEN:
Yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
No = ["No", "no", "NO", "nO", "N", "n"]

Valid = Yes + No
time.sleep(0.6)

print('''

 _____  ___         __      __  _              __    __  _____         
/__   \/___\/\ /\  /__\  /\ \ \/_\    /\/\    /__\/\ \ \/__   \        
  / /\//  // / \ \/ \// /  \/ //_\\\  /    \  /_\ /  \/ /  / /\/        
 / / / \_//\ \_/ / _  \/ /\  /  _  \/ /\/\ \//__/ /\  /  / /           
 \/  \___/  \___/\/ \_/\_\ \/\_/ \_/\/    \/\__/\_\ \/   \/            
                                                                       
           _   _____  ___                 _           _____    __  ___ 
  /\/\    /_\ /__   \/ __\ /\  /\/\/\    /_\    /\ /\ \_   \/\ \ \/ _ \\
 /    \  //_\\  / /\/ /   / /_/ /    \  //_\\\  / //_/  / /\/  \/ / /_\/
/ /\/\ \/  _  \/ / / /___/ __  / /\/\ \/  _  \/ __ \/\/ /_/ /\  / /_\\\ 
\/    \/\_/ \_/\/  \____/\/ /_/\/    \/\_/ \_/\/  \/\____/\_\ \/\____/ 
                                                                       

''')

time.sleep(0.3)
user_input = input("\n>> Start the Tournament? (Yes or No): ")

# VALIDATION CHECKS FOR STARTING OR NOT
while user_input not in Valid:
    time.sleep(0.3)
    user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")

while user_input in Yes:
    format_options = ["0", "1", "2"]
    time.sleep(0.3)
    print("\n=========================")
    print(">>> AVAILABLE FORMATS <<<")
    print("=========================")
    print("0) Leave Application")
    print("1) Double Round-Robin")
    print("2) Single Elimination")
    time.sleep(0.3)

    user_input_format = input("\n>> Select a Format: ")
    while user_input_format not in format_options:
        user_input_format = input("\n>> Invalid Input!: ")

    if user_input_format == "0":
        break

    time.sleep(0.3)
    print("\n>> Starting the Tournament!")
    time.sleep(0.5)
    print(">> Please Wait...")
    time.sleep(2)

    if user_input_format == "1":
        Double_Round_Robin.match_making()
    elif user_input_format == "2":
        Single_Elimination.match_making()

    time.sleep(0.3)
    user_input = input("\n>> Start a New Tournament? (Yes or No): ")
    while user_input not in Valid:
        time.sleep(0.3)
        user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")
    if user_input in No:
        time.sleep(0.3)
        user_input = input("\n>> Confirm? (Yes or No): ")
        while user_input not in Valid:
            time.sleep(0.3)
            user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")
        if user_input in Yes:
            break
        else:
            user_input = "Yes"

time.sleep(0.6)
print("""

   ____  __ _____  __________    __  ___   _____        __     ___   _              __ 
  /__\ \/ / \_   \/__   \_   \/\ \ \/ _ \ /__   \/\  /\/__\   / _ \ /_\    /\/\    /__\\
 /_\  \  /   / /\/  / /\// /\/  \/ / /_\/   / /\/ /_/ /_\    / /_\///_\\\  /    \  /_\  
//__  /  \/\/ /_   / //\/ /_/ /\  / /_\\\   / / / __  //__   / /_\\\/  _  \/ /\/\ \//__  
\__/ /_/\_\____/   \/ \____/\_\ \/\____/   \/  \/ /_/\__/   \____/\_/ \_/\/    \/\__/  


""")
time.sleep(3)
