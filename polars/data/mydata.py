import os
import csv

path = os.path.join(os.path.dirname(__file__), "../../data/")

files = {
    "age_house_value": f"{path}age_house_value.csv",
    "age_income": f"{path}age_income.csv",
    "city_avg_income": f"{path}city_avg_income.csv",
    "cohort_retention_data": f"{path}cohort_retention_data.csv",
    "imdb_movies": f"{path}imdb_movies.csv",
    "movie_metadata": f"{path}movie_metadata.csv",
    "name_children": f"{path}name_children.csv",
}
