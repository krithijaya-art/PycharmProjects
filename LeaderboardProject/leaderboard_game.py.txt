leaderboard = {}

while True:
    print("\n1. Add Score\n2. Show Leaderboard\n3. Check Rank\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        player = input("Enter player name: ")
        score = int(input("Enter score: "))
        if player in leaderboard:
            leaderboard[player]['score'] += score
        else:
            leaderboard[player] = {'score': score}
        print("Score updated.")

    elif choice == "2":
        if leaderboard:
            print("\n--- Leaderboard ---")
            sorted_board = sorted(leaderboard.items(), key=lambda x: x[1]['score'], reverse=True)
            rank = 1
            for player, data in sorted_board:
                print(f"{rank}. {player} - {data['score']} points")
                rank += 1
        else:
            print("Leaderboard is empty!")

    elif choice == "3":
        player_name = input("Enter player name: ")
        sorted_board = sorted(leaderboard.items(), key=lambda x: x[1]['score'], reverse=True)
        rank = 1
        found = False
        for name, data in sorted_board:
            if name == player_name:
                print(f"{player_name} is ranked {rank} with {data['score']} points.")
                found = True
                break
            rank += 1
        if not found:
            print(f"{player_name} is not on the leaderboard yet.")

    elif choice == "4":
        print("Exiting the game. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
