import time
from datetime import datetime

import pandas
import requests

# This file needs to be executed first.
# Afterwards, run the `get_commits.py` file with your authentication

def generate_csv(filename):
    df = pandas.DataFrame(columns=['repository_ID', 'name', 'URL', 'created_date',
                          'description', 'Language', 'number_of_stars', 'type', 'created_at', 'forks_count', 'issues_count', 'topics_count'])

    idx_count = 0
    page_count = 1
    search_query = '>500'

    while idx_count < 2500:
        req_repo = f'https://api.github.com/search/repositories?q=stars:{search_query}&sort=stars&order=desc&per_page=100&page={page_count}'

        result = requests.get(req_repo,
                              auth=("<username>", "<password>")).json()

        for repo in result['items']:
            temp = {'repository_ID': repo['id'],
                    'name': repo['name'],
                    'full_name': repo['full_name'],
                    'URL': repo['html_url'],
                    'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                    'created_at': repo['created_at'],
                    'Language': repo['language'],
                    'number_of_stars': repo['stargazers_count'],
                    'type': repo['owner']['type'],
                    'forks_count': repo['forks_count'],
                    'issues_count': repo['open_issues_count'] if repo['has_issues'] else 0,
                    'topics_count': len(repo['topics']) } 

            temp_df = pandas.DataFrame(temp, index=[idx_count])
            df = pandas.concat([df, temp_df])
            print(f"Number of indexed results: {idx_count}")
            print(f"Indexed: {temp['name']} and star count: {temp['number_of_stars']}")
            idx_count = idx_count + 1

            if (idx_count % 1000 == 0):
                last_stars = repo['stargazers_count'] - 1
                search_query = f"500..{last_stars}"
                print(f"1000 results reached, starting new query at {last_stars} stars...")
                page_count = 0

        page_count = page_count + 1

    print('Final dataframe result:')
    print(df)
    df.to_csv(f'datasets/{filename}.csv')
    print(f'Saved as {filename}.csv')


if __name__ == '__main__':
    generate_csv('test')
