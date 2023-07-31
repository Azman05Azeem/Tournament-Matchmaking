# #IMPORTED LIBRARIES
import time
import random
import Features


def main():
    # Instructions for Operator
    time.sleep(0.5)
    print("")
    print("====================")
    print(">>> INSTRUCTIONS <<<")
    print("====================")
    time.sleep(0.7)
    print("- Min Players/Teams: 2")
    time.sleep(1)
    print("- Enter 'Start' to Start Matchmaking.")
    time.sleep(1)
    print("- Number of Players must be in 'Power' of '2' (2, 4, 8, 16...)")
    time.sleep(1)
    print("- Winner will progress while Loser will be given a chance, else Eliminated.")
    time.sleep(1)
    print("- Last '2' Contestants will Compete For the Trophy!")
    time.sleep(1)

    # Player Entry
    player_list = Features.player_entry(True)
    player_count = len(player_list)

    # Player-list Shuffled
    random.shuffle(player_list)

    # Generate Pairs
    if player_count == 2:
        pairs = player_list
    else:
        time.sleep(1)
        pairs = generate_pairs(player_list)

    # Starting Rounds
    time.sleep(0.5)
    print("\n==========================")
    print(">>> TOURNAMENT MATCHES <<<")
    print("==========================")
    time.sleep(1)
    print(">> Matchmaking in Progress...")
    time.sleep(1)
    print(">> Let's Start!")
    time.sleep(0.5)

    if player_count == 2:
        time.sleep(0.5)
        print("\n>> Moving To Finals... This Happened Because Only 'Two' Players Joined the Pool.")
        time.sleep(1)
        Features.finals([player_list, player_count])
    else:
        game_manager(pairs)


def generate_pairs(players_list):  # Function to Generate Pairs
    try:
        num_players = len(players_list)
        match_pairs = []
        for i in range(0, num_players, 2):
            match_pairs.append((players_list[i], players_list[i + 1]))

        return match_pairs

    except IndexError:
        return players_list[0]


def game_manager(initial_pairs):
    def game_rounds_manager(pairs, is_winner_round):  # Runs the Matchmaking Messaging / Updating System
        winners = []  # Stores Winners
        last_chance_players = []  # Stores Last chance players
        eliminated = []  # Stores Eliminated

        # Count Match Number
        match_number_a = 0  # For Managing Round-Schedule
        match_number_b = 0  # For Managing Round-Information

        if len(pairs) > 1:  # Displays Round Schedule
            print("\n======================")
            print(">>> ROUND SCHEDULE <<<")
            print("======================")

            for schedule in pairs:
                time.sleep(0.5)
                print(">> Match #" + str(match_number_a + 1) + ": " + schedule[0] + " vs " + schedule[1])
                match_number_a += 1

        for Temp in pairs:  # Matches Between Players
            time.sleep(0.5)
            print("\n=========================")
            print(">>> MATCH INFORMATION <<<")
            print("=========================")

            if len(pairs) > 2:
                print(f">> Match #{match_number_b + 1}: " + Temp[0] + " vs " + Temp[1])
            else:
                print(">> Match: " + Temp[0] + " vs " + Temp[1])

            match_number_b += 1

            time.sleep(1)  # Updating Scoreboard
            print("\n=========================")
            print(">>> SCOREBOARD UPDATE <<<")
            print("=========================")
            time.sleep(1)
            print("1) " + Temp[0])
            print("2) " + Temp[1])
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

            if is_winner_round:  # Sorts Required Information
                if user_input == "1":
                    winners.append(Temp[0])
                    last_chance_players.append(Temp[1])
                else:
                    winners.append(Temp[1])
                    last_chance_players.append(Temp[0])
            else:
                if user_input == "1":
                    last_chance_players.append(Temp[0])
                    eliminated.append(Temp[1])
                else:
                    last_chance_players.append(Temp[1])
                    eliminated.append(Temp[0])

            time.sleep(0.5)
            print("\n>> Updating...")
            time.sleep(1.5)
            print(">> Scoreboard Updated!")
            time.sleep(1)

        print("\n=====================")  # Summarises Player Performances
        print(">>> ROUND SUMMARY <<<")
        print("=====================")

        if len(winners) > 0:
            time.sleep(0.5)
            print(">> Winners Of the Round:")
            for Temp_a in winners:
                time.sleep(0.5)
                print(" - " + Temp_a)

            if len(last_chance_players) > 0:
                print("")

        if len(last_chance_players) > 0:
            time.sleep(0.5)
            print(">> Players with Last Chance:")
            for Temp_b in last_chance_players:
                time.sleep(0.5)
                print(" - " + Temp_b)

            if len(eliminated) > 0:
                print("")

        if len(eliminated) > 0:
            time.sleep(0.5)
            print(">> Players Eliminated: ")
            for Temp_c in eliminated:
                time.sleep(0.5)
                print(" - " + Temp_c)

        return [winners, last_chance_players]  # Returns information for next Round

    game_rounds = 0  # Counts Number of Rounds

    next_round_winners_pairs = []  # Stores Pairs For Next Winner's Round
    next_round_last_chance_pairs = []  # Stores Pairs For Next Elimination Round

    buffer_one = ""  # Temporary Storage To Manage Complexities

    semi_finalists = []  # Stores Semi Finalist Pairs
    semi_final_flag = False  # Flag To Start Semi-Finals

    final_one = ""  # Finalist #1
    final_two = ""  # Finalist #2
    final_flag = False  # Flag To Start Finals

    if game_rounds == 0:  # First Round
        print("\n===================")
        print(">>> FIRST ROUND <<<")
        print("===================")
        time.sleep(0.5)
        print(">> An Important Round! This is where everyone starts their Game!")
        time.sleep(1)
        information = game_rounds_manager(initial_pairs, True)  # Index [0] = Winners, Index [1] = Last-Chance

        # Creating Pairs For Next Round
        next_round_winners_pairs = generate_pairs(information[0])
        next_round_last_chance_pairs = generate_pairs(information[1])
        time.sleep(1)
        game_rounds += 1

    # Runs The Tournament after First Game
    if game_rounds > 0:
        winner_loop_flag = True  # Winner's Round Flag
        last_chance_loop_flag = True  # Elimination Round Flag

        while True:
            this_round_last_chance_pairs = next_round_last_chance_pairs  # Reference to Previous Round Information

            if winner_loop_flag:  # Winner's Round
                print("\n======================")
                print(">>> WINNER'S ROUND <<<")
                print("======================")
                time.sleep(0.5)
                print(f">> [Round #{game_rounds + 1}] Winners of Previous Round complete with each-other. "
                      f"They get a 'Chance' if they lose.")
                time.sleep(1)
                information_winner = game_rounds_manager(next_round_winners_pairs, True)

                # Checks if it is possible to run Winner's Round
                if len(information_winner[0]) == 1:
                    final_one = information_winner[0][0]
                    time.sleep(0.5)
                    print(f"\n>> {final_one} has reached Finals! They wait for an Opponent!")
                    buffer_one = information_winner[1][0]
                    winner_loop_flag = False
                else:
                    next_round_winners_pairs = generate_pairs(information_winner[0])
                    next_round_last_chance_pairs = generate_pairs(information_winner[1])

            if last_chance_loop_flag:  # Elimination Round
                time.sleep(1)
                print("\n=========================")
                print(">>> ELIMINATION-ROUND <<<")
                print("=========================")
                time.sleep(0.5)
                print(f">> [Round #{game_rounds + 1}] Eliminating Players if they lose. "
                      f"This is their last chance to 'Redeem' themselves!")
                time.sleep(1)

                information_last_chance = game_rounds_manager(this_round_last_chance_pairs, False)

                # Checks if Elimination Round can be Further Run.
                if winner_loop_flag:
                    next_round_last_chance_pairs.extend(generate_pairs(information_last_chance[1]))
                else:  # Runs Qualifier Round incase Winner's Round cannot Proceed Further
                    if len(information_last_chance[1]) != 1:
                        equality_flag = False
                        while True:
                            time.sleep(0.5)
                            print("\n=======================")
                            print(">>> QUALIFIER-ROUND <<<")
                            print("=======================")
                            print(">> Addition Rounds... Finals are Near!")
                            time.sleep(1)
                            next_pairs = information_last_chance[1]

                            # Manages Unequal pairs, No Need for Semi-Finals after this Case
                            if len(next_pairs) % 2 != 0 and (not equality_flag) and (
                                    len(information_last_chance[1]) != 1):
                                time.sleep(0.5)
                                print("\n>> Matchmaking System has detect 'Irregularities'. Thereby,"
                                      " matches are re-adjusted, so there will 'No Semi-Finals'!")

                                time.sleep(2)
                                next_pairs.append(buffer_one)  # Semi-Finalist For Adjustment
                                information_last_chance = game_rounds_manager(generate_pairs(next_pairs), False)
                                equality_flag = True

                            # Manages Unequal pairs if it occurs more than once
                            elif equality_flag and (len(next_pairs) % 2 != 0) and (
                                    len(information_last_chance[1]) != 1):
                                time.sleep(0.5)
                                print(f"\n>> {final_one} is coming for a Tie-Break! This Happened due to "
                                      f"'Un-Equality' in Number of Players! They are still Finalist!")

                                time.sleep(0.5)
                                next_pairs.append(final_one)  # Finalist For Adjustment
                                information_last_chance = game_rounds_manager(generate_pairs(next_pairs), False)

                                if final_one in information_last_chance[1]:  # Removes Finalist (incase they win)
                                    information_last_chance[1].remove(final_one)

                                if len(information_last_chance[1]) == 1:
                                    final_two = information_last_chance[1][0]
                                    last_chance_loop_flag = False
                                    final_flag = True
                                    break

                            else:  # Runs Qualifier Rounds until Only 'One' Player is Left
                                information_last_chance = game_rounds_manager(generate_pairs(next_pairs), False)

                                if len(information_last_chance[1]) == 1 and (not equality_flag):
                                    buffer_two = information_last_chance[1][0]
                                    semi_finalists = [buffer_one, buffer_two]
                                    last_chance_loop_flag = False
                                    semi_final_flag = True
                                    break
                                elif equality_flag and (len(information_last_chance[1]) == 1):
                                    final_two = information_last_chance[1][0]
                                    last_chance_loop_flag = False
                                    final_flag = True
                                    break

                    # Direct Semi-Finals in case of Lesser Players (4 Players, Tested)
                    elif len(information_last_chance[1]) == 1:
                        buffer_two = information_last_chance[1][0]
                        semi_finalists = [buffer_one, buffer_two]
                        last_chance_loop_flag = False
                        semi_final_flag = True

            # Runs Semi Final Rounds
            if semi_final_flag and (not winner_loop_flag) and (not last_chance_loop_flag):
                time.sleep(1)
                print("\n=========================")
                print(">>> SEMI-FINALS ROUND <<<")
                print("=========================")
                print(">> Winner Competes with the Player at Finals!")
                time.sleep(0.5)
                information_semi_final = game_rounds_manager(generate_pairs(semi_finalists), False)
                final_two = information_semi_final[1][0]
                final_flag = True
                break

            elif final_flag and (not semi_final_flag) and (not winner_loop_flag) and (not last_chance_loop_flag):
                break

            game_rounds += 1

    # Final Match
    if final_flag:
        Features.finals([[final_one, final_two], ["EMPTY"]])
