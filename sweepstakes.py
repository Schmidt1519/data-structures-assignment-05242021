import random

class Sweepstakes:
    def __init__(self):
        self.contestants = {1: "Michael Jordan"}

    def add_contestants(self):
        self.contestants[2] = "LeBron James"
        self.contestants[3] = "Kareem Abdul-Jabbar"
        self.contestants[4] = "Wilt Chamberlain"
        self.contestants[5] = "Bill Russell"

    def winner(self):
        entry_list = list(self.contestants.values())
        select_winner = random.choice(entry_list)
        print(select_winner)