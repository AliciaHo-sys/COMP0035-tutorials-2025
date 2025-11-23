""" Starter for activity 5.4 Pydantic classes with validation """
from datetime import date
from enum import Enum

from pydantic import BaseModel
from pydantic import ValidationError

 


# This is not a Pydantic class! It is an Enum https://docs.python.org/3/library/enum.html
class MedalType(Enum):
    BRONZE = 3
    SILVER = 2
    GOLD = 1


class Medal(BaseModel):
    """ Represents a Medal

    Attributes:
        type (MedalType):  A string representing "gold", "silver", "bronze"
        date_won (date):  Date the medal was won

    """
    type: MedalType
    date_won: date | None


class Athlete(BaseModel):
    """ Represents an Athlete

        Attributes:
            first_name (str): The first name of the athlete.
            last_name (str): The last name of the athlete.
            team_code (str): The team code the athlete represents.
            disability_class (str): The disability classification of the athlete.

        Methods:
            introduce(): Prints an introduction of the athlete.
    """
    first_name: str #Must be provided
    last_name: str # Must be provided
    team_code: str | None # Optional, can be None
    disability_class: str |None # Optional, can be None
    medals: list[Medal] = [] # Set to empty as default

    def introduce(self) -> str:
        """
                Prints an introduction of the athlete, including their name, team, and disability class.
                """
        return f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}."


class ParalympicEvent(BaseModel):
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         register_athlete() Adds an athlete to the list of athletes

     """
    name: str
    sport: str
    classification: str
    athletes: list[Athlete]

    def register_athlete(self, athlete: Athlete):
        """ Register the athlete with the event

        Args:
            athlete (Athlete): The athlete to register
        """
        self.athletes.append(athlete)

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
    medal1 = Medal(type=1, date_won=date(2023, 7, 1))
    
    medal2 = Medal(type=1, date_won= None)

    medal3 = Medal(type=3, date_won= None)
    # Create an athlete with medals
    """"
    athlete = Athlete(
        first_name="Wei",
        last_name="Wang",
        team_code="CHN",
        disability_class="T54",
        medals=[medal1, medal2]
    )
    """
    
    try:
        bp = Athlete(first_name="Bianka", medals=1)
    except ValidationError as e:
        print("this is an error", e.errors())
    
    
    athlete_none = Athlete(
        first_name="Alicia",
        last_name="HO",
        team_code="HK",
        disability_class = "",
        medals = []
    )

    athlete_none_1 = Athlete(
        first_name="Catherine",
        last_name="Debrunner",
        team_code="ITA",
        disability_class = "",
        medals = []
    )
    
    for i in range (6):
        athlete_none.medals.append(medal1) 
    print(athlete_none)

    for i in range (5):
        athlete_none_1.medals.append(medal2)
    print(athlete_none_1)
    athlete_none_1.medals.append(medal3)
    
    #Catherine Debrunner from ITA Italy won 5 gold and 1 bronze
    #print(athlete)
    
    #print(medal1)
       
    

   
if __name__ == "__main__":
    main()

