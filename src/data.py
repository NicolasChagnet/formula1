from src import config
from sqlalchemy import create_engine, text
import pandas as pd
import cachetools

# Create a cache object.
cache = cachetools.TTLCache(maxsize=100, ttl=60)

# SQL engine
engine = create_engine(f"sqlite:///{config.dbfile}")


# def split_sql_statements(queries):
#     """Splits a string containing multiple sql queries into a list of queries"""
#     queries_list = queries.split(";")
#     queries_list_fixed = [query + ";" for query in queries_list if len(query) > 0]
#     return queries_list_fixed


@cachetools.cached(cache)
def get_data_query_file(filename, **kws):
    """Given a query_name, reads the appropriate .sql query file and loads the output in a dataframe.
    Optional parameters `variable=value` can be given in order to replace placeholder statements ":variable" in the SQL query.
    """

    # Connect to SQL database
    with engine.begin() as conn:
        connection = conn.connection
        # Open the query file and loads the result in a dataframe
        with open(config.path_queries / f"{filename}.sql", "r") as query_file:
            query = query_file.read()
            # Replace the placeholder parameters with variables
            for key, val in kws.items():
                query = query.replace(":" + key, str(val))
            df = pd.read_sql_query(query, engine)
    return df


def make_fullname(df):
    df["fullname"] = df["driver_forename"] + " " + df["driver_surname"]


def get_list_drivers(year):
    list_driver_year = get_data_query_file("list_drivers_year", year_chosen=year)
    make_fullname(list_driver_year)
    return list_driver_year
