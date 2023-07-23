# #IMPORTED LIBRARIES
import time
import random


def match_making():
    def player_entry():
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
        print("- Min Players/Teams: 2.")
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
            user_input_player = input(">> Team/Player #" + str(playercount + 1) + "'s Name: ")
            time.sleep(0.5)

            # Stops Entering Names After the following is Entered
            if user_input_player in ["", " "]:
                print(">> Invalid Input!")
            elif user_input_player in playerlist:
                print(">> This Name Already Exists!")
            elif user_input_player in ["Start", "START", "start"]:
                if playercount >= 2 and (playercount & (playercount - 1) == 0):
                    break
                elif playercount & (playercount - 1) != 0:
                    print(">> Number of Players Must be in Power of 2! (2, 4, 8, 16...)")
                else:
                    print(">> Insufficient Players/Teams to start Matchmaking! (Minimum: '2 Players'):")

            else:
                playerlist.append(user_input_player)
                playerscore.append(0)
                playercount += 1

        # Player-list Shuffled
        random.shuffle(playerlist)

        # Generate Pairs
        pairs = generate_match_pairs(playerlist)

        # Starting Rounds
        time.sleep(0.5)
        print("\n==========================")
        print(">>> TOURNAMENT MATCHES <<<")
        print("==========================")
        time.sleep(1)
        print(">> Matchmaking in Progress...")
        time.sleep(1)
        print(">> Let's Start!")
        game_rounds(pairs)

    def generate_match_pairs(playerslist):
        try:
            num_players = len(playerslist)
            match_pairs = []
            for i in range(0, num_players, 2):
                match_pairs.append((playerslist[i], playerslist[i + 1]))

            return match_pairs

        except IndexError:
            return False

    def game_rounds(pairs):
        stage_number = 0
        previous = 0

        winners = []
        losers = []
        time.sleep(0.5)

        while True:
            print("\n=================")
            print(">>> STAGE # " + str(stage_number+1) + " <<<")
            print("=================")
            time.sleep(1)
            stage_number += 1
            match_number = 0
            print(">> Match Schedule:")

            for Temp in pairs:
                print(">> Round#" + str(match_number + 1) + ": " + Temp[0] + " vs " + Temp[1])
                time.sleep(1)
                match_number += 1

            match_number = 0
            time.sleep(1)
            print("\n>> Starting the Game...")

            if previous == 2:
                print("\n===================")
                print(">>> Final Round <<<")
                print("===================")
            elif previous == 4:
                print("\n========================")
                print(">>> Semi-Final Round <<<")
                print("========================")
            else:
                print("\n===================")
                print(">>> MATCHMAKING <<<")
                print("===================")

            for rounds in pairs:
                time.sleep(0.5)

                print(">> Match #" + str(match_number + 1) + ": " + rounds[0] + " vs " + rounds[1])

                match_number += 1

                time.sleep(1)
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

                if user_input == "1":
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
            print(">> Qualified Players: ")
            for Temp_a in winners:
                time.sleep(1)
                print("- " + Temp_a)

            print("\n>> Eliminated Players:")
            for Temp_b in losers:
                time.sleep(1)
                print("- " + Temp_b)

            pairs = generate_match_pairs(winners)

            if not pairs:
                announcement(winners[0], losers[0])
                break

            previous = len(winners)
            winners = []
            losers = []

    def announcement(winner, loser):
        time.sleep(0.5)
        print("\n=========================")
        print(">>> END OF TOURNAMENT <<<")
        print("=========================")
        time.sleep(1)
        print(">> The Tournament Has Come To an End!")
        time.sleep(1)
        print(">> '" + winner + "' is the Winner of This Competition!")
        time.sleep(1)
        print(">> '" + loser + "' Gave a Great Competition to " + "'" + winner + "'!")
        time.sleep(1)

    player_entry()
