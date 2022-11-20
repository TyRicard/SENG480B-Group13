import time
import sys
import pandas as pd
import requests


def get_commits(file_in, file_out):
    # The approach was taken from the following source:
    # 1./ https://gist.github.com/yershalom/a7c08f9441d1aadb13777bce4c7cdc3b
    commits = pd.read_csv(f"../data/datasets/{file_in}")
    commits['commit_count'] = 0

    for i in range(0, 2500):
        full_name = commits['full_name'].iloc[i]

        # First get the latest commit request: https://docs.github.com/en/rest/commits/commits
        last_commit_req = f"https://api.github.com/repos/{full_name}/commits?per_page=1&order=desc"
        result = requests.get(last_commit_req)

        # Second, determine the last page. Because there is a single commit per page, the last page would be
        # the commit total. The reges is similar to the source.
        if result.headers.get('Link'):
            commit_count = int(result.headers.get('Link').split(',')[1].split('=')[3].split('>')[0])
            commits['commit_count'].iloc[i] = commit_count
            print(commit_count)

        if (i != 0 and i % 1000 == 0):
            print(f"1000 results reached, waiting to avoid rate limit...")
            for remaining in range(360, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

    print(commits)
    commits.to_csv(f'datasets/{file_out}')


if __name__ == '__main__':
    get_commits('nov20_data.csv', 'git_commits.csv')
