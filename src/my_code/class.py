class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes

     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names


    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)

class Athlete:
    def __init__(self, name, team, disa_classification):
        self.name = name
        self.team = team
        self.dis_classification = disa_classification
        self.athletes = []

    def __str__(self):
        """ Describes the event """
        return f"{self.name} is of {self.team} team for classification {self.dis_classification}."
        

    

def main():
    """
    event = ParalympicEvent(
    name="Men's individual BC1",
    sport="Boccia",
    classification="BC1",
    )
    event.describe()  # Should print the event description, "Athletes competing" will be empty
    event.register_athlete("Sungjoon Jung")  # should register the athlete
    event.describe()  # Should print the event again, "Athletes competing" should include Sungjoon Jung
    """
    athlete = Athlete("Alicia", "HK", "blindness")
    print(str(athlete))
       


   
if __name__ == "__main__":
    main()
