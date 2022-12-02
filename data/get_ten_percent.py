import time
import sys
import pandas as pd
import requests
import math
import datetime as dt
from dateutil.parser import parse # https://stackabuse.com/converting-strings-to-datetime-in-python/


def get_ten_percent(file_in, file_out):
    # The approach was taken from the following source:
    # 1./ https://stackoverflow.com/questions/61836313/github-api-number-of-stars-of-a-repository-over-time
    dataframe = pd.read_csv(f"../data/datasets/{file_in}")
    dataframe['ten_percent_star'] = 0.0

    # Get the current time for time delta calculation
    current_date = dt.datetime.now(dt.timezone.utc)

    for i in range(0, 2500):
        full_name = dataframe['full_name'].iloc[i]

        # First, get the total amount of stars and then get the half-way point.
        total_star_count = dataframe['number_of_stars'].iloc[i]
        ten_star_count = math.floor(total_star_count * 0.1)

        # Second, get the date of the half-star count making an api call.
        count_req = f"https://api.github.com/repos/{full_name}/stargazers?page={ten_star_count}&per_page=1"
        headers = {'Accept': 'application/vnd.github.v3.star+json'}
        result = requests.get(count_req, auth=("<username>", "<password>"), headers=headers).json()

        # To do the calculation, get the time of the milestone star, the repo's creation_date, and current_time
        if result:
            milestone_star_date = parse(result[0]['starred_at'])
            repo_create_date = parse(dataframe['created_at'].iloc[i])
            milestone_diff = current_date - milestone_star_date
            repo_diff = current_date - repo_create_date
            ratio = 1 - (milestone_diff / repo_diff)
            print(ratio)
            dataframe['ten_percent_star'].iloc[i] = ratio

    dataframe.to_csv(f'datasets/{file_out}')


if __name__ == '__main__':
    get_ten_percent('preprocess_data.csv', 'RQ3_data.csv')
