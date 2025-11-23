from datetime import date

from sqlmodel import Field, SQLModel, Column, Relationship, create_engine

from sqlalchemy import CheckConstraint, ForeignKey

from typing import Optional

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
# Optional[str/int] value may be either a str/int or None
class Country(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country: str 
    teams: list["Team"] = Relationship(back_populates="country")


class Disability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str 

class Team(SQLModel, table=True):
    code: str | None = Field(default=None, primary_key=True)
    name: str 
    region: Optional[str] = Field(
        sa_column=Column("region", CheckConstraint
                         ("region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')"))
        )
    sub_region: Optional[str]
    member_type: Optional[str] = Field(sa_column=Column("member_type", CheckConstraint
                                              ("member_type IN ('country', 'team', 'dissolved', 'construct')"))
                            )
    notes: Optional[str] 
    country_id: Optional[int] = Field(
        default= None, 
        sa_column= Column (ForeignKey("country.id", onupdate = "CASCADE", ondelete = "SET NULL"))
        )
    country: "Country" = Relationship(back_populates="teams")

