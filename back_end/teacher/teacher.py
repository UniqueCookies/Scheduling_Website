class Teacher:
    def __init__(self, name, availability, preference):
        self.name = name
        self.availability = availability
        self.preference = preference

    def __str__(self):
        return f"Teacher: {self.name}\nAvailability: {self.availability}\nPreference: {self.preference}"
