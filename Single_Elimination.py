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
    print("- Winner will progress while Loser will be eliminated.")
    time.sleep(1)
    print("- Last '2' Contestants will Compete For the Trophy!")
    time.sleep(1)

    # Player Entry
    player_list = Features.player_entry(True)

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
        if len(pairs) > 2:
            print(">> Match Schedule:")

            for Temp in pairs:  # Game Scheduling
                print(">> Match #" + str(match_number + 1) + ": " + Temp[0] + " vs " + Temp[1])
                time.sleep(1)
                match_number += 1
        else:
            print(">> Qualifying Rounds! Important For Finals!")

        match_number = 0

        for rounds in pairs:  # Matches Between Players / Entry for Winner or Loser
            time.sleep(0.5)

            if previous != 2:
                print("\n===================")
                print(">>> MATCHMAKING <<<")
                print("===================")
                if len(pairs) > 2:
                    print(">> " + rounds[0] + " vs " + rounds[1])
                else:
                    print(f">> Match #{match_number + 1}: " + rounds[0] + " vs " + rounds[1])
            else:
                print(f"\n>> Final Match #{match_number + 1}: " + rounds[0] + " vs " + rounds[1])
                time.sleep(1)

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

            if user_input == "1":  # Winners / Losers Filter
                winners.append(rounds[0])
                losers.append(rounds[1])
            else:
                losers.append(rounds[0])
                winners.append(rounds[1])

            if previous != 2:
                time.sleep(0.5)
                print("\n>> Updating...")
                time.sleep(1.5)
                print(">> Scoreboard Updated!\n")
                time.sleep(1)
                print("====================")
                print(">>> END OF STAGE <<<")
                print("====================")
                time.sleep(1)

        # Lists Players that have Qualified / Eliminated
        if previous != 2:
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
            Features.announcement(winners[0], losers[0])
            break

        previous = len(winners)

        winners = []
        losers = []
