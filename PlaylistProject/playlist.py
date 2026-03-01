

playlist = {}

while True:
    print("\n--- Personalized Playlist Manager ---")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Search Song")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter song title: ").strip()
        artist = input("Enter artist name: ").strip()

        if title in playlist:
            print("This song is already in the playlist!")
        else:
            playlist[title] = artist
            print(f"'{title}' by {artist} added to the playlist.")

    elif choice == "2":
        title = input("Enter song title to remove: ").strip()

        if title in playlist:
            del playlist[title]
            print(f"'{title}' removed from the playlist.")
        else:
            print("Song not found in the playlist!")

    elif choice == "3":
        if playlist:
            print("\nYour Playlist:")
            for title, artist in playlist.items():
                print(f"- {title} by {artist}")
        else:
            print("Your playlist is empty!")

    elif choice == "4":
        search = input("Enter song title to search: ").strip().lower()

        found = False
        for title, artist in playlist.items():
            if search in title.lower():
                print(f"'{title}' is in your playlist, sung by {artist}.")
                found = True
        if not found:
            print("Song not found in the playlist!")

    elif choice == "5":
        print("Exiting Playlist Manager. Have a great day!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
