from pathlib import Path

from pyprojroot.here import (
    here,
)  # This package is useful to track the root directory of the package

random_state = 314159  # Random state for reproducibility

# Useful locations of files

root_folder = here()

path_data = root_folder / "data"
path_data_raw = path_data / "raw"
path_data_final = path_data / "final"
path_log = root_folder / "log" / "out.log"
path_queries = root_folder / "queries"
path_index = root_folder / "templates" / "index.html"

dbfile = path_data_final / "formula1.db"
seasons = (1950, 2024)
default_year = seasons[1]

nationality_map = {
    "British": "gb",
    "German": "de",
    "Spanish": "es",
    "Finnish": "fi",
    "Japanese": "jp",
    "French": "fr",
    "Polish": "pl",
    "Brazilian": "br",
    "Italian": "it",
    "Australian": "au",
    "Austrian": "at",
    "American": "us",
    "Dutch": "nl",
    "Colombian": "co",
    "Portuguese": "pt",
    "Canadian": "ca",
    "Indian": "in",
    "Hungarian": "hu",
    "Irish": "ie",
    "Danish": "dk",
    "Argentine": "ar",
    "Czech": "cz",
    "Malaysian": "my",
    "Swiss": "ch",
    "Belgian": "be",
    "Monegasque": "mc",
    "Swedish": "se",
    "Venezuelan": "ve",
    "New Zealander": "nz",
    "Chilean": "cl",
    "Mexican": "mx",
    "South African": "za",
    "Liechtensteiner": "li",
    "Rhodesian": "zw",
    "American-Italian": "us",
    "Uruguayan": "uy",
    "Argentine-Italian": "ar",
    "Thai": "th",
    "East German": "de",
    "Russian": "ru",
    "Indonesian": "id",
    "Chinese": "cn",
}

country_map = {
    "Australia": "au",
    "Malaysia": "my",
    "Bahrain": "bh",
    "Spain": "es",
    "Turkey": "tr",
    "Monaco": "mc",
    "Canada": "ca",
    "France": "fr",
    "UK": "gb",
    "Germany": "de",
    "Hungary": "hu",
    "Belgium": "be",
    "Italy": "it",
    "Singapore": "sg",
    "Japan": "jp",
    "China": "cn",
    "Brazil": "br",
    "USA": "us",
    "United States": "us",
    "UAE": "ae",
    "Argentina": "ar",
    "Portugal": "pt",
    "South Africa": "za",
    "Mexico": "mx",
    "Korea": "kr",
    "Netherlands": "nl",
    "Sweden": "se",
    "Austria": "at",
    "Morocco": "ma",
    "Switzerland": "ch",
    "India": "in",
    "Russia": "ru",
    "Azerbaijan": "az",
    "Saudi Arabia": "sa",
    "Qatar": "qa",
}
