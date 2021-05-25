class Pi:
    def __init__(self):
        self.months = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")


    def month_of_pi_day(self):
        for item in self.months:
            if item == "March":
                print(f'{item} contains Pi day.')