class Schedule:
    def __init__(self, section, period):
        self.section = section
        self.period = period
        self.matrix = [[None for _ in range(period)] for _ in range(section)]
    def display(self):
        for row in self.matrix:
            print(row)