from sqlmodel import Session

from .a_database import create_db_and_tables, engine
from .a_model import Country, Team, Disability

"""
def create_heroes():
    with Session(engine) as session:
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team=team_z_force
        )
        session.add(hero_deadpond)
        session.commit()

        session.refresh(hero_deadpond)

        print("Created hero:", hero_deadpond)
        print("Hero's team:", hero_deadpond.team)
"""

def create_para():
    with Session(engine) as session:
        country_uk = Country(country="United Kingdom")
        country_us = Country(country="United States")

        team_uk_paralympics = Team(
            code="GBR",
            name="Great Britain Paralympic Team",
            region="Europe",
            sub_region="Northern Europe",
            member_type="country",
            notes="Represents the United Kingdom",
            country=country_uk
        )

        team_us_paralympics = Team(
            code="USA",
            name="United States Paralympic Team",
            region="America",
            sub_region="Northern America",
            member_type="country",
            notes="Represents the United States",
            country=country_us
        )

        session.add(team_uk_paralympics)
        session.add(team_us_paralympics)
        session.commit()

        print("Created teams:", team_uk_paralympics, team_us_paralympics)

def main():
    create_db_and_tables()
    create_para()


if __name__ == "__main__":
    main()