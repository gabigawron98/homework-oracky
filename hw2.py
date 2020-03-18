from typing import List
import pandas as pd
import datetime
import os

# confirmed cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
dfC = pd.read_csv(url, error_bad_lines=False)

# deaths
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
dfD = pd.read_csv(url, error_bad_lines=False)

# recovered cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
dfR = pd.read_csv(url, error_bad_lines=False)


# Helper function (strftime not cross platform) ???
def format_date(date: datetime.date):
    if os.name == "nt":
        return date.strftime('%#m/%#d/%y')
    else:
        return date.strftime('%-m/%-d/%y')


def countries_with_no_deaths_count(date: datetime.date) -> int:
    """
    Returns the number of areas (countries, region, provinces) in the data set
    where infections were found, but nobody died on a given date. (DO NOT GROUP BY)
    Ex.
    >>> countries_with_no_deaths_count(datetime.date(2020, 3, 15))
    171
    >>> countries_with_no_deaths_count(datetime.date(2020, 2, 18))
    46
    :param date: Date object of the date to get the results for
    :return: Number of countries with no deaths but with active cases on a given date as an integer
    """
    
    # Your code goes here
    pass


def more_cured_than_deaths_indices(date: datetime.date) -> List[int]:
    """
    Returns table indices of areas (countries, region, provinces) in the data set
    with more cured cases than deaths on a given date. (DO NOT GROUP BY)
    Ex.
    >>> more_cured_than_deaths_indices(datetime.date(2020, 3, 15))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19,
    21, 24, 25, 27, 28, 29, 30, 32, 33, 34, 37, 38, 40, 41, 43, 44,
    45, 46, 53, 55, 58, 59, 60, 62, 64, 65, 68, 86, 92, 101, 110, 118,
    128, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
    168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
    183, 184, 185, 187, 188, 189, 190, 191, 192, 193, 194, 202, 208]
    >>> more_cured_than_deaths_indices(datetime.date(2020, 2, 18))
    [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 15, 18, 19, 20, 92, 154, 156,
    157, 158, 159, 160, 161, 162, 163, 164, 166, 167, 168, 169, 171, 172,
    173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 187,
    188, 189, 190, 191, 192, 193, 194, 202, 347, 348, 403]
    :param date: Date object of the date to get the results for
    :return: A List of integers containing indices of countries which had more cured cases than deaths on a given date
    """
    
    # Your code goes here
    pass