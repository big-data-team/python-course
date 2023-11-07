import pandas as pd
import typing as tp
import os


class PandasDataProcessor:
    """
    A class that is able to process, filter and join pandas dataframes.
    """

    def __init__(self, work_dir):
        self.work_dir = work_dir

    def load_data(self, filename: str) -> pd.DataFrame:
        """
        Loads data into memory. Supports file with .csv or .parquet formats.
        Raises Value error if other format is provided.
        """

        """
        YOUR CODE HERE
        """
        pass

    def join_two_dataframes_vertically(
        self, data_a: pd.DataFrame, data_b: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Join 2 dataframes vertically. data_a is followed by data_b.
        Number of rows will be equal to length or rows from data_a + length of rows from data_b.
        Number of columns will not change. Makes sure indices of the data are reset.
        """

        """
        YOUR CODE HERE
        """
        pass

    def join_two_dataframes_horizontally(
        self, data_a: pd.DataFrame, data_b: pd.DataFrame
    ) -> pd.DataFrame:
        """
        joins data horizontally. Number of rows in the resulting dataframe should stay the same.
        Number of columns will be a union of columns from data_a and data_b/
        """

        """
        YOUR CODE HERE
        """
        pass

    def filter_data_by_chain_of_rules(
        self, data: pd.DataFrame, filter_rules: tp.List[tp.Tuple[str, tp.Any]]
    ) -> pd.DataFrame:
        """
        Takes as input a dataframe and a chain of filter rules. Filters data by all rules.

        Each filter rule is expressed as a tuple where 1st elem of a tuple is a column name and a 2nd is a column value.
        E.g. ("revenue", 100) filter rule means one needs to select all rows of data where column "revenue" has a value of 100.

        Apply filters one by one. Return data after all filters are applied. Make sure indices are reset.
        """

        """
        YOUR CODE HERE
        """
        pass

    def join_two_dataframes_by_common_columns(
        self,
        data_a: pd.DataFrame,
        data_b: pd.DataFrame,
        join_type: str,
        join_columns: tp.List[str],
    ) -> pd.DataFrame:
        """
        join_type should be one of "left", "right", "inner", "outer", "cross".
        Raises Value Error if some other join type is passed.

        join_columns is passed as list to provide an ability to join on one or multiple columns.

        In the end function joins data_a and data_b with given params and returns joined df. Indiced are reset.
        """

        """
        YOUR CODE HERE
        """
        pass

    def join_two_dataframes_with_different_keys(
        self,
        data_a: pd.DataFrame,
        data_b: pd.DataFrame,
        data_a_key_col: str,
        data_b_key_col: str,
    ) -> pd.DataFrame:
        """
        Joins 2 dataframes on different key names.
        E.g. in the data_a column may be named "ID" and in the data_b it can be named "id",
        this method should be able to process such cases.
        In the end remove data_b_key_col from the joined datafame.
        """

        """
        YOUR CODE HERE
        """
        pass

    def compute_financial_stats(
        self, filename: str, groupby_col: str, stat_col: str
    ) -> tp.Dict[str, int]:
        """
        - loads data from existing load_data method
        - removes rows where costs is null
        - fill null values of revenue with a median of revenue
        - create profit column as revenue minus costs
        - removes rows where profut <=0
        - groups data by groupby_col
        - computes mean value for each group, casts it to INT
        - returns results as dict
        """

        """
        YOUR CODE HERE
        """

        pass
