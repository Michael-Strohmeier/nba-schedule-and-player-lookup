import pandas as pd
from util import url_to_soup
import unicodedata


class Roster:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters"

        self.teams = self.get_team_rosters()

    def get_team_rosters(self):
        soup = url_to_soup(self.url)

        tables = soup.find_all("table", {"class": "toccolours"})

        d = dict()
        for table in tables:
            # team_name
            team_name = table.find("div", {"class": "navbar-header"}).b.text
            team_name = team_name.replace(" roster", "")

            uls = table.find_all("ul")

            # head_coach
            head_coach = uls[1].find("li").text

            # assistant_coaches
            assistant_coaches = []
            for li in uls[2]:
                try:
                    assistant_coaches.append(li.text)
                except:
                    continue

            # players
            players = []

            player_table = table.find("tbody").find("tbody")
            for tr in player_table.find_all("tr"):
                temp = []
                for td in tr.find_all("td"):
                    temp.append(td.text)

                if temp:
                    temp = [unicodedata.normalize("NFKD", t).strip().split(" (")[0] for t in temp]
                    players.append(temp)

            d[team_name] = {
                "head_coach": head_coach,
                "assistant_coaches": assistant_coaches,
                "players": pd.DataFrame(players,
                                        columns=["position", "number", "name", "height", "weight", "dob", "from"])
            }

        return d

    def find_players_team(self, player_name: str):
        temp = []

        for nba_team in self.teams.keys():
            players = list(self.teams[nba_team]["players"]["name"])

            for player in players:
                if player_name.lower() in player.lower():
                    temp.append([player, nba_team])

        return temp
