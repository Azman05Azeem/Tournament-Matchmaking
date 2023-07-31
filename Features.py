# #IMPORTED LIBRARIES
import time


# CONFIRMATION - For Entry, Continue etc...
def confirm():
    yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
    no = ["No", "no", "NO", "nO", "N", "n"]

    valid = yes + no

    time.sleep(0.5)
    user_input = input(">> Confirm? (Yes or No): ")

    while user_input not in valid:
        time.sleep(0.3)
        user_input = input(">> Invalid Input! Enter 'Yes' or 'No': ")

    if user_input in yes:
        flag = True
    else:
        flag = False

    time.sleep(0.5)
    return flag


def player_entry(is_elimination_flag):
    player_list = []
    player_count = 0

    # Player Entry
    print("\n====================")
    print(">>> PLAYER ENTRY <<<")
    print("====================")

    while True:
        time.sleep(0.5)
        if player_count > 0:
            print("")
        user_input_player = input(">> Team/Player #" + str(player_count + 1) + "'s Name: ")
        time.sleep(0.5)

        # Validation Checks for Player Name Entry
        if user_input_player in ["", " "]:
            print(">> Invalid Input!")
        elif user_input_player in player_list:
            print(">> This Name Already Exists!")
        elif user_input_player in ["Start", "START", "start"]:
            if player_count < 2:
                print(">> Insufficient Players/Teams to start Matchmaking! (Minimum: '2 Players'):")
            elif is_elimination_flag:
                if player_count >= 2 and (player_count & (player_count - 1) == 0):
                    confirm_flag = confirm()
                    if confirm_flag:
                        break
                    else:
                        time.sleep(0.5)
                        print(">> Processing... Please Wait!")
                        time.sleep(1.5)
                elif player_count & (player_count - 1) != 0:
                    print(">> Number of Players Must be in Power of 2! (2, 4, 8, 16...)")
            elif not is_elimination_flag:
                if player_count >= 2:
                    confirm_flag = confirm()
                    if confirm_flag:
                        break
                    else:
                        time.sleep(0.5)
                        print(">> Processing... Please Wait!")
                        time.sleep(1.5)
        else:
            confirm_flag = confirm()
            if confirm_flag:
                player_list.append(user_input_player)
                player_count += 1

    return player_list


def announcement(winner, runner):
    time.sleep(0.5)
    print("\n>> The Winner has 'Redeemed' themselves! ")
    time.sleep(1)
    print("\n==================================")
    print(">>> CHAMPION OF THE TOURNAMENT <<<")
    print("==================================")
    time.sleep(0.5)
    print(">> The Winner of the Tournament is: " + winner)
    time.sleep(1)
    print("\n===================================")
    print(">>> RUNNER-UP OF THE TOURNAMENT <<<")
    print("===================================")
    time.sleep(0.5)
    print(">> The Most Challenging: " + runner)
    time.sleep(1)
    print("\n>> Congratulations to '" + winner + "' and '" + runner + "' for coming this close!")
    time.sleep(1)
    print(">> And a Big-Thanks to 'Every' participants! See you all around in next Tournament!")
    time.sleep(1.5)
    print("\n==============================")
    print(">>> END OF THE TOURNAMENT <<< ")
    print("==============================")
    time.sleep(1)


def sort(players_list, players_score, flag_next_stage, number):  # Generates Scoreboard & Displays it
    # Player Scores
    score = [players_list, players_score]

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
            time.sleep(0.3)
            player_name = sorted_scoreboard[0][i]
            player_score = sorted_scoreboard[1][i]
            print(i + 1, end=") ")
            print(f"{player_name}: {player_score}")
    else:
        player_list = []
        players_score = []

        # Prints Qualified Players/Team Names (Top-2 or Top-4 on Scoreboard):
        for i in range(number):
            time.sleep(0.3)
            player_name = sorted_scoreboard[0][i]
            player_list.append(player_name)
            player_score = sorted_scoreboard[1][i]
            players_score.append(player_score)
            print(i + 1, end=") ")
            print(f"{player_name}: {player_score}")

        qualified = [player_list, players_score]
        return qualified

    time.sleep(1.5)


def finals(player_data):  # Manages Finals Round
    time.sleep(1)
    print("\n===================")
    print(">>> FINAL ROUND <<<")
    print("===================")
    time.sleep(0.5)
    print(">> Intensive Final Match Between: '" + str(player_data[0][0]) + "' & '" + str(player_data[0][1]) + "'")
    time.sleep(2)
    print(">> Wishing Both Opponents GoodLuck!")
    time.sleep(1)
    print("\n=========================")
    print(">>> SCOREBOARD UPDATE <<<")
    print("=========================")
    print("1) " + player_data[0][0])
    print("2) " + player_data[0][1])
    time.sleep(1)

    while True:
        user_input = input("\n>> Winner of Match: ")

        while user_input not in ["1", "2"]:  # Validating Input
            user_input = input(">> Invalid Input!: ")

        confirm_flag = confirm()
        if confirm_flag:
            break
        else:
            time.sleep(0.5)
            print(">> Processing... Please Wait!")
            time.sleep(1.5)

    if user_input == "1":
        champion = player_data[0][0]
        runner = player_data[0][1]
    else:
        champion = player_data[0][1]
        runner = player_data[0][0]

    announcement(champion, runner)
