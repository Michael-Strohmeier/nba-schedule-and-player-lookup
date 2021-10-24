from roster import Roster
from season import Season


if __name__ == '__main__':
    season = Season()
    roster = Roster()

    while True:
        i = int(input("Enter to search [1: Player, 2: Team]: "))
        if i == 1:
            s = input("Enter player name: ")
            print(roster.find_players_team(s))
            print("\n")
        else:
            s = input("Enter team name: ")
            print(season.find_team_games(s))
            print("\n")

