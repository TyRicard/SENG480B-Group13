import os
import pandas as pd
import requests

# The approach was taken from the following source:
# 1./ https://gist.github.com/yershalom/a7c08f9441d1aadb13777bce4c7cdc3b
commits = pd.read_csv("../data/datasets/data.csv")
commits['commit_count'] = 0

for i in range(0,2500):
    full_name = commits['full_name'].iloc[i]

    # First get the latest commit request: https://docs.github.com/en/rest/commits/commits
    last_commit_req = "https://api.github.com/repos/{full_name}/commits?per_page=1&order=desc"
    result = requests.get(last_commit_req)

    # Second, determine the last page. Because there is a single commit per page, the last page would be 
    # the commit total. The reges is similar to the source.
    if result.headers.get('Link'):
        commit_count = int(result.headers.get('Link').split(',')[1].split('=')[3].split('>')[0])
        commits['commit_count'].iloc[i] = commit_count
        print(commit_count)

print(commits)
commits.to_csv('datasets/git_commits.csv')
