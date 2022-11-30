import time
import sys
import pandas as pd
import requests

def get_contributors(file_in, file_out):
    # The approach was taken from the following source:
    # 1./ https://stackoverflow.com/questions/36410357/github-v3-api-list-contributors
    contributors = pd.read_csv(f"../data/datasets/{file_in}")
    contributors['contributor_count'] = 0

    for i in range(0, 2500):
        full_name = contributors['full_name'].iloc[i]

        contributors_req = f"https://api.github.com/repos/{full_name}/contributors?anon=1&page=1&per_page=1"
        result = requests.get(contributors_req, auth=("<username>", "<token>"))

        # Second, determine the last page. Because there is a single contributor per page, the last page would be
        # the commit total. The regex is similar to the source.
        if result.headers.get('Link'):
            contributor_count = int(result.headers.get('Link').split(',')[1].split('=')[2].split('&')[0])
            contributors['contributor_count'].iloc[i] = contributor_count
            print(contributor_count)

    contributors.to_csv(f'datasets/{file_out}')


if __name__ == '__main__':
    get_contributors('data.csv', 'git_contributors.csv')
