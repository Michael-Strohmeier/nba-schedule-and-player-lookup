import pandas as pd
import time
from typing import List
import datetime
from util import url_to_soup


class Season:
    def __init__(self):
        self.season = "2022"
        self.raw_games = self.get_season_games()
        self.df = pd.DataFrame(self.raw_games, columns=["date", "away", "home", "time"])

        self.setup()

    def get_games(self, month: str, season: str) -> List:
        url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games-{month}.html"
        soup = url_to_soup(url)

        table = soup.find("tbody")
        rows = table.find_all("tr")

        games = []
        for row in rows:
            temp = []

            for a in row.find_all("a"):
                temp.append(a.text)

            temp = temp[:3]

            temp.append(row.find("td", {"data-stat": "game_start_time"}).text)

            games.append(temp)

        return games

    def get_season_games(self):
        months = ["october", "november", "december", "january", "february", "march", "april"]

        games = []
        for month in months:
            games.extend(self.get_games(month, self.season))
            time.sleep(0.2)

        return games

    def setup(self):
        months = {"oct": 10,
                  "nov": 11,
                  "dec": 12,
                  "jan": 1,
                  "feb": 2,
                  "mar": 3,
                  "apr": 4}

        temp = []
        for date in self.df["date"]:
            date = date.replace(",", "").split(" ")

            month = date[1].lower()
            month = months[month]
            day = int(date[2])
            year = int(date[3])

            temp.append(datetime.date(year, month, day))

        self.df["datetime"] = temp

    def get_future_games(self):
        today = datetime.date.today()
        return self.df[self.df["datetime"] >= today]

    def find_team_games(self, team_name: str) -> pd.DataFrame:
        temp_df = self.get_future_games()
        temp = temp_df[temp_df[["away", "home"]].applymap(lambda x: team_name in x).any(1)]

        return temp[["date", "time", "away", "home"]][:5]