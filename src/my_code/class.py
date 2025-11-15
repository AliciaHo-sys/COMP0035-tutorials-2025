from dataclasses import dataclass
from datetime import date
from typing import List



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
         

# Base class
@dataclass
class Medals:
    type: str
    design: str
    date_designed: date
    


# Subclass
class Athlete:

    def __init__(self, first_name: str, last_name: str, team_code: str, disability_class: str, medals: List[Medals]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals # Composition: Athlete has Medals

    def __str__(self):
        """ Describes the event """
        return f"{self.first_name} {self.last_name} is of {self.team_code} team has {self.medals}."


    

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
    #athlete = Athlete("Alicia", "HK", "blindness")
    #print(str(athlete))
    # Create medals
    medal1 = Medals( "gold", "Paris 2024 design", date(2023, 7, 1))
    medal2 = Medals("silver",  "Tokyo 2020 design", date(2019, 8, 25))

    # Create an athlete with medals
    
    athlete = Athlete(
        first_name="Wei",
        last_name="Wang",
        team_code="CHN",
        disability_class="T54",
        medals=[medal1, medal2]
    )
   
    print(athlete)
    #print(medal1)
       
    

   
if __name__ == "__main__":
    main()
