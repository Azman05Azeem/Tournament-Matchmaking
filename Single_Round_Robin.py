# #IMPORTED LIBRARIES:
import time
import random
import Features


# #FUNCTIONS:
def main():
    player_score = []  # Stores Player's Score

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
    player_list = Features.player_entry(False)
    player_count = len(player_list)

    # Player Score
    for Temp in range(len(player_list)):
        player_score.append(0)

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
        Features.finals([player_list, player_score])


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
                    val = random.randint(0, 1000)
                    if val % 2 == 0:
                        pair_temp = (Temp_a, Temp_b)
                    else:
                        pair_temp = (Temp_b, Temp_a)
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
            time.sleep(0.5)
            print("\n>> Updating...")
            time.sleep(1.5)
            print(">> Scoreboard Updated!")
            time.sleep(0.5)
            Features.sort(player_list, player_score, False, 0)

        current_pairs = []

        time.sleep(0.5)
        if rounds == 1 and (player_count > 4):
            print("\n>> Players Qualifying For Semi-Finals:")
            time.sleep(0.5)
            qualified = Features.sort(player_list, player_score, True, 4)
            player_list_a = qualified[0]
            current_pairs = [(player_list_a[0], player_list_a[1]), (player_list_a[0], player_list_a[1])]
            player_score = qualified[1]

        if rounds > 1 or (player_count <= 4):
            print("\n>> Players Qualifying For Finals:")
            time.sleep(0.5)
            qualified = Features.sort(player_list, player_score, True, 2)
            time.sleep(0.5)
            Features.finals(qualified)
            break
