# #IMPORTED LIBRARIES
import time
import random


def match_making():
    def player_entry():
        player_list = []  # Stores Player's Name
        player_count = 0  # Counts Number of Players

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
        print("- Winner will progress while Loser will be eliminated.")
        time.sleep(1)
        print("- Last '2' Contestants will Compete For the Trophy!")
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
                if player_count >= 2 and (player_count & (player_count - 1) == 0):  # Checks if the Player Count is 2^X.
                    break
                elif player_count & (player_count - 1) != 0:
                    print(">> Number of Players Must be in Power of 2! (2, 4, 8, 16...)")
                else:
                    print(">> Insufficient Players/Teams to start Matchmaking! (Minimum: '2 Players'):")

            else:
                player_list.append(user_input_player)
                player_count += 1

        # Player-list Shuffled
        random.shuffle(player_list)

        # Generate Pairs
        pairs = generate_match_pairs(player_list)

        # Starting Rounds
        time.sleep(0.5)
        print("\n==========================")
        print(">>> TOURNAMENT MATCHES <<<")
        print("==========================")
        time.sleep(1)
        print(">> Matchmaking in Progress...")
        time.sleep(1)
        print(">> Let's Start!\n")
        game_rounds(pairs)

    def generate_match_pairs(players_list):  # Function to Generate Pairs
        try:
            num_players = len(players_list)
            match_pairs = []
            for i in range(0, num_players, 2):
                match_pairs.append((players_list[i], players_list[i + 1]))

            return match_pairs

        except IndexError:
            return False

    def game_rounds(pairs):  # Runs The Game
        stage_number = 0  # Number of Stages
        previous = 0  # Temporary, Stores Record of Previous Data

        winners = []  # Winners are listed here
        losers = []  # Losers are listed here
        time.sleep(0.5)

        if len(pairs) == 1:  # Manages Messages to Display/ Game Mechanics incase '4' or '2' players are Pooled.
            previous = 2
            print(">> Moving to 'Finals' Because Only '2' Players Participated.")
        elif len(pairs) == 2:
            previous = 4
            print(">> Moving to 'Semi-Finals' Because Only '4' Players Participated.")

        while True:  # Loops / Runs the Tournaments until a Winner is Found
            match_number = 0
            time.sleep(1)
            print("\n>> Starting the Game...")

            if previous == 2:  # Decides Messages according to stage of the Game
                print("\n===================")
                print(">>> FINAL STAGE <<<")
                print("===================")
                time.sleep(0.5)
            elif previous == 4:
                print("\n========================")
                print(">>> SEMI-FINAL STAGE <<<")
                print("========================")
                time.sleep(0.5)
            else:
                print("\n=================")
                print(">>> STAGE # " + str(stage_number + 1) + " <<<")
                print("=================")
                time.sleep(1)

            stage_number += 1
            print(">> Match Schedule:")

            for Temp in pairs:  # Game Scheduling
                print(">> Match #" + str(match_number + 1) + ": " + Temp[0] + " vs " + Temp[1])
                time.sleep(1)
                match_number += 1

            match_number = 0

            for rounds in pairs:  # Matches Between Players / Entry for Winner or Loser
                time.sleep(0.5)
                print("\n===================")
                print(">>> MATCHMAKING <<<")
                print("===================")
                print(">> " + rounds[0] + " vs " + rounds[1])

                match_number += 1

                time.sleep(1)  # Updating Scoreboard
                print("\n=========================")
                print(">>> SCOREBOARD UPDATE <<<")
                print("=========================")
                time.sleep(1)
                print("1) " + rounds[0])
                print("2) " + rounds[1])
                time.sleep(1)
                time.sleep(0.5)
                user_input = input("\n>> Winner of Match: ")

                while user_input not in ["1", "2"]:
                    user_input = input("\n>> Invalid Input!: ")

                if user_input == "1":  # Winners / Losers Filter
                    winners.append(rounds[0])
                    losers.append(rounds[1])
                else:
                    losers.append(rounds[0])
                    winners.append(rounds[1])

                time.sleep(0.5)
                print(">> Updating...")
                time.sleep(1.5)
                print(">> Scoreboard Updated!\n")
                time.sleep(1)

            print("====================")
            print(">>> END OF STAGE <<<")
            print("====================")
            time.sleep(1)

            # Lists Players that have Qualified / Eliminated
            print(">> Qualified Players: ")
            for Temp_a in winners:
                time.sleep(1)
                print(" - " + Temp_a)

            print("\n>> Eliminated Players:")
            for Temp_b in losers:
                time.sleep(1)
                print(" - " + Temp_b)

            # Pairs the Winners
            pairs = generate_match_pairs(winners)

            # Ends the Matchmaking incase a Winner is Declared
            if not pairs:
                announcement(winners[0], losers[0])
                break

            previous = len(winners)
            winners = []
            losers = []

    def announcement(winner, loser):  # Announces Winners
        time.sleep(0.5)
        print("\n=========================")
        print(">>> END OF TOURNAMENT <<<")
        print("=========================")
        time.sleep(1)
        print(">> The Tournament Has Come To an End!\n")
        time.sleep(1)
        print(">> '" + winner + "' is the Winner of This Competition!")
        time.sleep(1)
        print(">> '" + loser + "' Gave a Tough Competition to " + "'" + winner + "'!")
        time.sleep(1)

    player_entry()
