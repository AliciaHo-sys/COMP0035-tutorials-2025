# Placeholder for pytest fixtures
import pytest
from activities.starter.playing_cards import Suit, Rank, Deck
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel.pool import StaticPool
from activities.starter.playing_cards import create_cards


@pytest.fixture
def deck_cards():
    suit_values = [Suit(suit=s) for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']]
    rank_values = [Rank(rank=str(r)) for r in
                   [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']]
    deck_cards = Deck(suits=suit_values, ranks=rank_values)
    yield deck_cards


@pytest.fixture(name="session")
def session_fixture():
    # Create the cards
    suits, ranks, cards = create_cards()

    # Create the session and yield
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        # Add the objects to the database
        session.add_all(suits)
        session.add_all(ranks)
        session.add_all(cards)
        session.commit()
        yield session