class Birthday:
    def __init__(self):
        self.bday_locations = {"Kansas City", "Minneapolis", "Denver"}


    def birthday_locations(self):
        self.bday_locations.update(["Chicago", "Las Vegas", "Dallas"])

        for each_item in self.bday_locations:
            print(each_item)