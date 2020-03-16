from typing import List
from datetime import timedelta

import re
import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def get_date_str(day: int, month: int, year: int = 2020):
    if not 1 <= day <= 31 or not 1 <= month <= 12 or not 2000 <= year <= 2020:
        raise ValueError("Incorrect arguments")
    return str(month) + '/' + str(day) + '/' + str(year)[2:]


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    """
    Returns confirmed infection cases for country 'Poland' given a date.
    Ex.
    >>> poland_cases_by_date(7, 3, 2020)
    5
    >>> poland_cases_by_date(11, 3)
    31
    :param year: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param day: Day of month to get the cases for as an integer indexed from 1
    :param month: Month to get the cases for as an integer indexed from 1
    :return: Number of cases on a given date as an integer
    """
    country_col_name = "Country/Region"
    
    date = get_date_str(day, month, year)
    poland_data = confirmed_cases.loc[confirmed_cases[country_col_name] == "Poland"]
    return poland_data[date].iloc[0]


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    """
    Returns the top 5 infected countries given a date (confirmed cases).
    Ex.
    >>> top5_countries_by_date(27, 2, 2020)
    ['China', 'Korea, South', 'Cruise Ship', 'Italy', 'Iran']
    >>> top5_countries_by_date(12, 3)
    ['China', 'Italy', 'Iran', 'Korea, South', 'France']
    :param day: 4 digit integer representation of the year to get the countries for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: A list of strings with the names of the coutires
    """
    country_col_name = "Country/Region"

    date = get_date_str(day, month, year)
    infections_per_country = confirmed_cases[[country_col_name, date]].groupby([country_col_name]).sum()
    ranking = infections_per_country.sort_values(by=date, ascending=False).head(5)
    return list(ranking.index)


# Function name is wrong, read the pydoc
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    """
    Returns the number of countries/regions where the infection count in a given day
    was NOT the same as the previous day.
    Ex.
    >>> no_new_cases_count(11, 2, 2020)
    35
    >>> no_new_cases_count(3, 3)
    57
    :param day: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: Number of countries/regions where the count has not changed in a day
    """
    date_format = '%m/%d/%y'
    country_col_name = "Country/Region"

    date = get_date_str(day, month, year)
    prev_date = (pd.datetime.strptime(date, date_format) - timedelta(days=1)).strftime(date_format)
    prev_date = re.sub(r"^0", "", prev_date)
    prev_date = re.sub(r"/0", "/", prev_date)
    infections_per_country = confirmed_cases[[country_col_name, date, prev_date]]
    filtered_data = infections_per_country.loc[infections_per_country[date] != infections_per_country[prev_date]]
    return len(filtered_data.index)