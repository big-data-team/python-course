from collections.abc import Generator
from contextlib import closing
import sqlite3


def count_rows(sqlite_filepath: str, table_name: str) -> int:
    # your implementation is here
    return row_count


def generate_rows_from_table(sqlite_filepath: str, table_name: str) -> Generator[tuple]:
    # your implementation with yield is here
    pass


class MovieItem:
    # !!! do not change this class !!!
    def __init__(self, title: str, rating: float):
        self.title = title
        self.rating = rating

    def __repr__(self):
        outcome = f"{self.__class__.__name__}(title={self.title}, rating={self.rating})"
        return outcome

    def __eq__(self, rhs):
        outcome = (self.title == rhs.title) and (self.rating == rhs.rating)
        return outcome


def convert_movie_item(b_str) -> MovieItem:
    # your implementation is here

    # hint: you are working with bineary string, so
    # you will need to .decode("utf-8") from binary string
    # to get title
    pass


def register_converter():
    # your implementation is here

    # do the maigc with sqlite3 registration
    pass


def generate_movies_from_table(sqlite_filepath: str, table_name: str) -> Generator[MovieItem]:
    # !!! do not change SQL query !!!
    sql_query = f"select movie_title || ',' || rating AS 'm [movie_item]' from {table_name}"
    # ---

    # your implementation with yield is here
    # hint: you need to use detect_types
    # hint: you need to return MovieItem(s), not tuple((MovieItem,))
