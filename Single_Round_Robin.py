# #IMPORTED LIBRARIES:
import time
import random


# #FUNCTIONS:
def match_making():
    def player_entry():
        player_list = []  # Stores Player's Name
        player_score = []  # Stores Player's Data (Index Corresponds to player_list)
        player_count = 0  # Counts Number of Players

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
        print("- Group Stages are Played Initially. Players face each-other Once!")
        time.sleep(1)
        print("- Winner Gets '+2' Score, while Loser Gets '-1' Score. Draw has 'No Effect'.")
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
            user_input_player = input(">> Team/Player #" + str(player_count + 1) + "'s Name: ")
            time.sleep(0.5)

            # Validation Checks for Player Name Entry
            if user_input_player in ["", " "]:
                print(">> Invalid Input!")
            elif user_input_player in player_list:
                print(">> This Name Already Exists!")
            elif user_input_player in ["Start", "START", "start"]:
                if player_count >= 2:
                    break
                else:
                    print(">> Insufficient Players/Teams to start Matchmaking! (Minimum: '2 Players'):")
            else:
                player_list.append(user_input_player)
                player_score.append(0)
                player_count += 1

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

        # Filters if '2' Players
        if player_count != 2:
            game_manager(player_list, player_score, player_count)
        else:
            print("\n>> Moving Directly to Finals! This Happened Because Only 2 Players Joined the Pool!")
            time.sleep(1.5)
            finals([player_list])

    # noinspection PyUnresolvedReferences
    def game_manager(player_list, player_score, player_count):
        # Finds the Number of Matches Possible
        matches = 0
        for Temp_d in range(player_count - 1, 0, -1):
            matches = matches + Temp_d
        time.sleep(0.5)

        def generate_pairs(players):
            # Generates Pairs
            pairs = []  # Stores Pairs
            available_players = []  # Dummy List
            available_players.extend(players)  # Fills Dummy list with Player list Contents
            counter = 0  # Dummy Counter

            for Temp_a in players:
                counter += 1
                available_players.remove(Temp_a)
                if counter != player_count:
                    for Temp_b in available_players:
                        first = Temp_a
                        second = Temp_b
                        pair_temp = [first, second]
                        random.shuffle(pair_temp)
                        pairs.append(pair_temp)

            return pairs

        # Shuffles Pairs
        group_stage_pairs = generate_pairs(player_list)
        random.shuffle(group_stage_pairs)

        current_pairs = []
        rounds = 0

        # Starts the Competition
        while True:
            if rounds == 0:
                time.sleep(0.5)
                print("\n====================================")
                print(">>> STARTING GROUP STAGE MATCHES <<<")
                print("====================================")
                print(f">> Total Number of Matches: {matches}")
                rounds += 1

                # Schedule
                time.sleep(1)
                print("\n======================")
                print(">>> ROUND SCHEDULE <<<")
                print("======================")
                match_number = 0

                for schedule in group_stage_pairs:
                    time.sleep(0.5)
                    print(">> Match #" + str(match_number + 1) + ": " + schedule[0] + " vs " + schedule[1])
                    match_number += 1

                current_pairs.extend(group_stage_pairs)

            elif rounds == 1:
                time.sleep(0.5)
                print("\n=================")
                print(">>> SEMI FINALS <<<")
                print("===================")
                print(">> Players Competing for Top - 2 Spots!")
                rounds += 1

            # Running the Game
            current_match = 0

            for Temp_d in current_pairs:  # Matches Between Players
                loser = ""
                winner = ""
                current_match += 1
                time.sleep(1)
                print("\n=========================")
                print(">>> MATCH INFORMATION <<<")
                print("=========================")
                print(f">> Match #{current_match}: " + Temp_d[0] + " vs " + Temp_d[1])
                time.sleep(1)  # Updating Scoreboard
                print("\n=========================")
                print(">>> SCOREBOARD UPDATE <<<")
                print("=========================")
                time.sleep(1)
                print("0) Draw / Withdraw / Abandon")
                print("1) " + Temp_d[0])
                print("2) " + Temp_d[1])
                time.sleep(0.5)
                user_input = input("\n>> Winner of Match: ")
                time.sleep(0.5)

                while user_input not in ["0", "1", "2"]:  # Validating Input
                    user_input = input(">> Invalid Input!: ")

                if user_input == "1":
                    winner = Temp_d[0]
                    loser = Temp_d[1]
                elif user_input == "2":
                    winner = Temp_d[0]
                    loser = Temp_d[1]
                else:
                    time.sleep(0.5)
                    print("\n>> No Score to Change!")

                index_winner = player_list.index(winner)
                player_score[index_winner] += 2
                index_loser = player_list.index(loser)
                player_score[index_loser] -= 1

                sort(player_list, player_score, False, 0)

            current_pairs = []

            time.sleep(0.5)
            if rounds == 1 and (player_count != 4):
                print("\n>> Player Qualifying For Semi-Finals:")
                time.sleep(0.5)
                qualified = sort(player_list, player_score, True, 4)
                player_list_a = qualified[0]
                current_pairs = [(player_list_a[0], player_list_a[1]), (player_list_a[0], player_list_a[1])]
                player_score = qualified[1]

            if rounds > 1 or (player_count == 4):
                print("\n>> Player Qualifying For Finals:")
                time.sleep(0.5)
                qualified = sort(player_list, player_score, True, 2)
                time.sleep(0.5)
                finals(qualified)
                break

    def finals(player_data):  # Manages Finals Round
        time.sleep(2)
        print("\n===================")
        print(">>> FINAL ROUND <<<")
        print("===================")
        time.sleep(0.5)
        print(">> Intensive Final Match Between: '" + str(player_data[0][0]) + "' & '" + str(player_data[1][0]) + "'")
        time.sleep(2)
        print(">> Wishing Both Opponents GoodLuck!")
        time.sleep(1.5)
        print("\n=========================")
        print(">>> SCOREBOARD UPDATE <<<")
        print("=========================")
        print("1) " + player_data[0][0])
        print("2) " + player_data[1][1])
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
                    runner = player_data[1][0]
                else:
                    champion = player_data[1][0]
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
                print(i + 1, end=") ")
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
                print(i + 1, end=") ")
                print(f"{player_name}: {player_score}")

            qualified = [player_list, playerscore]
            return qualified

        time.sleep(1.5)

    player_entry()
