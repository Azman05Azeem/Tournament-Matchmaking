# #IMPORTED LIBRARIES:
import time
import random


# #FUNCTIONS:
def player_entry():  # Manages Matchmaking at Group Stages
    playerlist = []  # Stores Player's Name
    playerscore = []  # Stores Player's Data (Index Corresponds to player_list)

    playercount = 0  # Counts Number of Players

    # Instructions for Operator
    time.sleep(0.5)
    print("")
    print("====================")
    print(">>> INSTRUCTIONS <<<")
    print("====================")
    time.sleep(0.7)
    print("- Min Players/Teams: '2'.")
    time.sleep(1)
    print("- Enter 'Start' to Start Matchmaking.")
    time.sleep(1)
    print("- Group Stages are Played Initially. Players face each-other Twice!")
    time.sleep(1)
    print("- Winner Gets '+1' Score, while Loser Gets '-1' Score. Draw has no effect.")
    time.sleep(1)
    print("- Top '4' Contestants will Compete Each-other for the Semi-Finals!")
    time.sleep(1)
    print("- Top '2' Contestants will Compete For the Trophy!")
    time.sleep(1)

    # Player Entry
    print("\n====================")
    print(">>> PLAYER ENTRY <<<")
    print("====================")
    while True:
        time.sleep(0.5)
        user_input_player = input(">> Team/Player #" + str(playercount + 1) + "'s Name: ")
        time.sleep(0.5)

        # Stops Entering Names After the following is Entered
        if user_input_player in ["Start", "START", "start"]:
            if playercount >= 2:
                break
            else:
                print(">> Insufficient Players/Teams to start Matchmaking! (Minimum: '2 Players'):")
        else:
            playerlist.append(user_input_player)
            playerscore.append(0)
            playercount += 1

    # Player-list Shuffled
    random.shuffle(playerlist)

    if playercount != 2:
        group_stages(playerlist, playerscore, playercount)
    else:
        print("\n>> Moving Directly to Finals! This Happened Because Only 2 Players Joined the Pool!")
        time.sleep(1.5)
        finals([playerlist, playerscore])


def group_stages(player_list, player_score, player_count):
    player_combo = []  # Stores All The Opponents' Name (Index Corresponds to player_list)

    # This Algorithm Finds Possible Opponents For Each Player and Fills in 'player_combo' List
    for Temp_a in player_list:
        combo = []
        for Temp_b in player_list:
            if Temp_a != Temp_b:
                combo.append(Temp_b)

        # Combinations Shuffled - This Serves as Matchmaking's Base
        random.shuffle(combo)
        player_combo.append(combo)

    # Starts the Competition
    time.sleep(0.5)
    print("\n====================================")
    print(">>> STARTING GROUP STAGE MATCHES <<<")
    print("====================================")

    total_matches = 0  # Total Matches to be Played
    match_number = 0  # Current Match Being Played

    # Finding Total Number of Matches
    for Temp_c in range(len(player_combo[0])):
        for Temp_d in range(len(player_list)):
            total_matches += 1

    # Competition's Stats (For Information)
    time.sleep(1)
    print(">> Players/Team Registered: " + str(player_count))
    time.sleep(1)
    print(">> Total Games/Rounds: " + str(total_matches))
    time.sleep(2)
    print(">> Matchmaking in Process... Please Wait...")
    time.sleep(1.5)

    # Matchmaking Algorithm + Score Updating Mechanism
    for Temp_c in range(len(player_combo[0])):
        for Temp_d in range(len(player_list)):
            match_number += 1
            time.sleep(0.5)
            print("\n==================")
            print(">>> MATCH INFO <<<")
            print("==================")
            time.sleep(0.5)
            print(">> Match#" + str(match_number) + ": " + player_list[Temp_d] + " vs " + player_combo[Temp_d][Temp_c])
            time.sleep(1)
            try:
                print(">> " + player_list[Temp_d + 1] + " & " + player_combo[Temp_d + 1][Temp_c]
                      + " Will Play Next Round!")
            except IndexError:
                print(">> Matchmaking in Progress for More Rounds!")
            time.sleep(1.5)
            print("\n=========================")
            print(">>> SCOREBOARD UPDATE <<<")
            print("=========================")
            print("0) Match Drawn/Abandoned/Postponed")
            print("1) " + player_list[Temp_d])
            print("2) " + player_combo[Temp_d][Temp_c])
            print("")
            time.sleep(1)
            user_input = input(">> Winner of Match: ")

            while True:
                if user_input in ["0", "1", "2"]:
                    if user_input == "0":
                        time.sleep(0.5)
                        print(">> No Change To Scores!")
                        break
                    elif user_input == "1":
                        win = player_list[Temp_d]
                        lose = player_combo[Temp_d][Temp_c]
                    else:
                        win = player_combo[Temp_d][Temp_c]
                        lose = player_list[Temp_d]

                    for Temp_e in player_list:
                        if Temp_e == win:
                            index = player_list.index(Temp_e)
                            player_score[index] += 2
                        elif Temp_e == lose:
                            index = player_list.index(Temp_e)
                            player_score[index] -= 1

                    time.sleep(0.5)
                    print(">> Updating...")
                    time.sleep(1.5)
                    print("\n>> Scoreboard Updated!")
                    time.sleep(0.5)
                    print(">> Printing Scoreboard...")
                    time.sleep(1)
                    sort(player_list, player_score, False, 0)
                    break
                else:
                    time.sleep(0.5)
                    user_input = input(">> Invalid Input!: ")

    time.sleep(1)
    print("\n===========================")
    print(">>> END OF GROUP STAGES <<<")
    print("===========================")
    time.sleep(2)
    print("\n>> Qualified Players/Teams:")
    if player_count <= 4:
        qualified = sort(player_list, player_score, True, 2)  # Selects Top-2 Players (Player Count <= 4)
        time.sleep(1)
        print("\n>> Congratulations to Contestants! Wish You Good luck!")
        print(">> Moving on to Finals!")
        finals(qualified)
    elif player_count > 4:
        qualified = sort(player_list, player_score, True, 4)  # Selects Top-4 Players (Player Count > 4)
        time.sleep(1)
        print("\n>> Congratulations to Qualifiers! Wish You Good luck!")
        print(">> Moving on to Semi-Finals!")
        semi_finals(qualified)


def semi_finals(player_data):  # Manages Semi-Finals Round
    semi_score = []

    for Temp in range(4):
        semi_score.append(0)

    time.sleep(2)
    print("\n===================")
    print(">>> SEMI FINALS <<<")
    print("===================")
    print(">> GoodLuck To All Participants at this Stage!")
    print(">> Note: Semi-Finals will have its own Points Table!")
    time.sleep(1.5)
    print("\n>> Semi-Final #1 " + str(player_data[0][0]) + " vs " + str(player_data[0][1]))
    print(">> Semi-Final #2 " + str(player_data[0][2]) + " vs " + str(player_data[0][3]))
    for semi_round in range(2):
        if semi_round == 0:
            player_1 = player_data[0][0]
            player_2 = player_data[0][1]
        else:
            player_1 = player_data[0][2]
            player_2 = player_data[0][3]
        time.sleep(1)
        print("\n>> Round #" + str(semi_round+1) + ": " + player_1 + " vs " + player_2)
        time.sleep(1)
        print("\n=========================")
        print(">>> SCOREBOARD UPDATE <<<")
        print("=========================")
        print("1) " + player_1)
        print("2) " + player_2)
        print("")
        time.sleep(1)
        user_input = input(">> Winner of Match: ")
        while True:
            if user_input in ["1", "2"]:
                if user_input == "1":
                    win = player_1
                    lose = player_2
                else:
                    win = player_2
                    lose = player_1

                for Temp_e in player_data[0]:
                    if Temp_e == win:
                        index = player_data[0].index(Temp_e)
                        semi_score[index] += 2
                    elif Temp_e == lose:
                        index = player_data[0].index(Temp_e)
                        semi_score[index] -= 1

                time.sleep(0.5)
                print(">> Updating...")
                time.sleep(1.5)
                print("\n>> Scoreboard Updated!")
                time.sleep(0.5)
                print(">> Printing Scoreboard...")
                time.sleep(1)
                sort(player_data[0], semi_score, False, 0)
                break
            else:
                time.sleep(0.5)
                user_input = input(">> Invalid Input!: ")

    time.sleep(2)
    print("\n>> Qualified Players/Teams:")
    qualified = sort(player_data[0], semi_score, True, 2)  # Selects Top-2 Players (Player Count <= 4)
    time.sleep(1)
    print("\n>> Congratulations to Contestants! Wishing You all Good luck!")
    print(">> Moving on to Finals!")
    time.sleep(1)
    print("\n==========================")
    print(">>> END OF SEMI FINALS <<<")
    print("==========================")
    finals(qualified)


def finals(player_data):  # Manages Finals Round
    time.sleep(2)
    print("\n===================")
    print(">>> FINAL ROUND <<<")
    print("===================")
    time.sleep(0.5)
    print(">> Intensive Final Match Between: '" + str(player_data[0][0]) + "' & '" + str(player_data[0][1]) + "'")
    time.sleep(2)
    print(">> Wishing Both Opponents GoodLuck!")
    time.sleep(1.5)
    print("\n=========================")
    print(">>> SCOREBOARD UPDATE <<<")
    print("=========================")
    print("1) " + player_data[0][0])
    print("2) " + player_data[0][1])
    print("")
    time.sleep(1)
    user_input = input(">> Winner of Tournament: ")
    while True:
        if user_input in ["1", "2"]:
            time.sleep(1.5)
            print("\n>> The Winner has 'Redeemed' themselves! ")
            time.sleep(1)
            print("\n==================================")
            print(">>> CHAMPION OF THE TOURNAMENT <<<")
            print("==================================")
            if user_input == "1":
                champion = player_data[0][0]
                runner = player_data[0][1]
            else:
                champion = player_data[0][1]
                runner = player_data[0][0]
            break
        else:
            time.sleep(0.5)
            user_input = input(">> Invalid Input!: ")

    time.sleep(0.5)
    print(">> The Winner of the Tournament is: " + champion)
    time.sleep(1)
    print("\n===================================")
    print(">>> RUNNER-UP OF THE TOURNAMENT <<<")
    print("===================================")
    time.sleep(0.5)
    print(">> The Most Challenging: " + runner)
    time.sleep(1)
    print("\n>> Congratulations to '" + champion + "' and '" + runner + "' for coming this close!")
    time.sleep(1)
    print(">> And blessings to 'Every' participants! See you all around in next Tournament!")
    time.sleep(1.5)
    print("\n==============================")
    print(">>> END OF THE TOURNAMENT <<< ")
    print("==============================")
    time.sleep(1)


def sort(playerlist, playerscore, flag_next_stage, number):  # Generates Scoreboard & Displays it
    # Player Scores
    score = [playerlist, playerscore]

    # Transpose the scoreboard to group player names and their scores together
    transposed_scoreboard = list(zip(*score))

    # Sort the transposed scoreboard based on the scores (the second element of each sublist)
    sorted_scoreboard = sorted(transposed_scoreboard, key=lambda x: x[1], reverse=True)

    # Transpose the sorted scoreboard back to the original format
    sorted_scoreboard = list(zip(*sorted_scoreboard))

    if not flag_next_stage:
        # Print the sorted scoreboard
        print("\n==================")
        print(">>> SCOREBOARD <<<")
        print("==================")
        time.sleep(0.5)
        for i in range(len(sorted_scoreboard[0])):
            player_name = sorted_scoreboard[0][i]
            player_score = sorted_scoreboard[1][i]
            print(i+1, end=") ")
            print(f"{player_name}: {player_score}")
    else:
        player_list = []
        playerscore = []
        # Prints Qualified Players/Team Names (Top-2 or Top-4 on Scoreboard):
        for i in range(number):
            player_name = sorted_scoreboard[0][i]
            player_list.append(player_name)
            player_score = sorted_scoreboard[1][i]
            playerscore.append(player_score)
            print(i+1, end=") ")
            print(f"{player_name}: {player_score}")

        qualified = [player_list, playerscore]
        return qualified

    time.sleep(1.5)


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
    time.sleep(0.3)
    print("\n>> Starting the Tournament! (Format: Double Round-Robin)")
    time.sleep(0.5)
    print(">> Please Wait...")
    time.sleep(2)
    player_entry()
    time.sleep(0.3)
    user_input = input("\n>> Start Again? (Yes or No): ")
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

