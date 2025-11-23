from datetime import date

from sqlmodel import Field, SQLModel, Column, Relationship, create_engine

from sqlalchemy import CheckConstraint, ForeignKey

"""
class Games(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field()
    year: int
    start: date
    end: date
    countries: int
    events: int
    sports: int
    participants_m: int
    participants_f: int
    participants: int
    highlights: str
    URL: str
"""

class Country(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country: str 

class Disability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str 

class Team(SQLModel, table=True):
    code: str | None = Field(default=None, primary_key=True)
    name: str 
    region: str = Field(
        sa_column=Column("region", CheckConstraint
                         ("region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')"))
                        )
    sub_region: str 
    member_type: str = Field(sa_column=Column("member_type", CheckConstraint
                                              ("member_type IN ('country', 'team', 'dissolved', 'construct)"))
                            )
    notes: str 
    country_id: int = Field(sa_column= ForeignKey("country.id", onupdate = "CASCADE", ondelete = "NULL"))
    country: "Country" = Relationship(back_populates="teams")

engine = create_engine("sqlite:///paralympics_sqlmodel.db")

# 3. Create all the tables in the database
SQLModel.metadata.create_all(engine)