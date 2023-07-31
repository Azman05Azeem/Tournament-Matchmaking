# #IMPORTED LIBRARIES:
import time
import random
import Features


# #FUNCTIONS:
def main():
    player_score = []  # Stores Player's Data (Index Corresponds to player_list)

    # Instructions for Operator
    time.sleep(0.5)
    print("")
    print("====================")
    print(">>> INSTRUCTIONS <<<")
    print("====================")
    time.sleep(0.7)
    print("- Min Players/Teams: 2.")
    time.sleep(1)
    print("- Enter 'Start' to Start Matchmaking.")
    time.sleep(1)
    print("- Group Stages are Played Initially. Players face each-other Twice!")
    time.sleep(1)
    print("- Winner Gets '+2' Score, while Loser Gets '-1' Score. Draw has 'No Effect'.")
    time.sleep(1)
    print("- Top '4' Contestants will Compete Each-other for the Semi-Finals!")
    time.sleep(1)
    print("- Top '2' Contestants will Compete For the Trophy!")
    time.sleep(1)

    # Player Entry
    player_list = Features.player_entry(False)
    player_count = len(player_list)

    # Player Score
    for Temp in range(len(player_list)):
        player_score.append(0)

    # Player-list Shuffled
    random.shuffle(player_list)

    # Starting
    time.sleep(0.5)
    print("\n==========================")
    print(">>> TOURNAMENT MATCHES <<<")
    print("==========================")
    time.sleep(1)
    print(">> Matchmaking in Progress...")
    time.sleep(1)
    print(">> Let's Start!")
    time.sleep(0.5)

    if player_count != 2:
        group_stages(player_list, player_score, player_count)
    else:
        print("\n>> Moving Directly to Finals! This Happened Because Only 2 Players Joined the Pool!")
        time.sleep(1.5)
        Features.finals([player_list, player_score])


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
            print(">> Match #" + str(match_number) + ": " + player_list[Temp_d] + " vs " + player_combo[Temp_d][
                Temp_c])
            time.sleep(1)

            try:
                print(">> " + player_list[Temp_d + 1] + " & " + player_combo[Temp_d + 1][Temp_c]
                      + " Will Play Next Round!")
            except IndexError:
                time.sleep(0.5)

            time.sleep(1.5)
            print("\n=========================")
            print(">>> SCOREBOARD UPDATE <<<")
            print("=========================")
            print("0) Match Drawn/Abandoned/Postponed")
            print("1) " + player_list[Temp_d])
            print("2) " + player_combo[Temp_d][Temp_c])
            time.sleep(1)

            while True:
                user_input = input("\n>> Winner of Match: ")

                while user_input not in ["1", "2"]:  # Validating Input
                    user_input = input(">> Invalid Input!: ")

                confirm_flag = Features.confirm()

                if confirm_flag:
                    break
                else:
                    time.sleep(0.5)
                    print(">> Processing... Please Wait!")
                    time.sleep(1.5)

            win = ""
            lose = ""

            if user_input == "0":
                time.sleep(0.5)
                print(">> No Change To Scores!")
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
            print("\n>> Updating...")
            time.sleep(1)
            print(">> Scoreboard Updated!")
            time.sleep(0.5)
            Features.sort(player_list, player_score, False, 0)

    time.sleep(1)
    print("\n===========================")
    print(">>> END OF GROUP STAGES <<<")
    print("===========================")
    time.sleep(2)
    print("\n>> Qualified Players/Teams:")

    if player_count <= 4:
        qualified = Features.sort(player_list, player_score, True, 2)  # Selects Top-2 Players (Player Count <= 4)
        time.sleep(1)
        print("\n>> Congratulations to Contestants! Wishing You Good luck!")
        print(">> Moving on to Finals!")
        Features.finals(qualified)

    elif player_count > 4:
        qualified = Features.sort(player_list, player_score, True, 4)  # Selects Top-4 Players (Player Count > 4)
        time.sleep(1)
        print("\n>> Congratulations to Qualifiers! Wishing You Good luck!")
        print(">> Moving on to Semi Finals!")
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
        print("\n>> Round #" + str(semi_round + 1) + ": " + player_1 + " vs " + player_2)
        time.sleep(1)
        print("\n=========================")
        print(">>> SCOREBOARD UPDATE <<<")
        print("=========================")
        print("1) " + player_1)
        print("2) " + player_2)
        time.sleep(1)

        while True:
            user_input = input("\n>> Winner of Match: ")

            while user_input not in ["1", "2"]:  # Validating Input
                user_input = input(">> Invalid Input!: ")

            confirm_flag = Features.confirm()

            if confirm_flag:
                break
            else:
                time.sleep(0.5)
                print(">> Processing... Please Wait!")
                time.sleep(1.5)

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
        print("\n>> Updating...")
        time.sleep(1)
        print(">> Scoreboard Updated!")
        time.sleep(0.5)

        Features.sort(player_data[0], semi_score, False, 0)

    time.sleep(2)
    print("\n>> Qualified Players/Teams:")
    qualified = Features.sort(player_data[0], semi_score, True, 2)  # Selects Top-2 Players (Player Count <= 4)
    time.sleep(1)
    print("\n>> Congratulations to Contestants! Wishing You all Good luck!")
    print(">> Moving on to Finals!")
    time.sleep(1)
    print("\n==========================")
    print(">>> END OF SEMI FINALS <<<")
    print("==========================")
    Features.finals(qualified)
