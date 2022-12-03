import pandas as pd
import requests
import re
import os

# load token from environment file
# to use the script you need a .env file with your token and username exported as an environment variable
from dotenv import load_dotenv
load_dotenv()


def main():
    # Read in data from from datasets/data.csv
    # Remove any repo with more than 40000 stars
    repos = pd.read_csv("../data/datasets/data.csv")
    repos = repos.drop(repos[repos.number_of_stars >= 40000].index)

    # For every remaining repo
    # Use the 'Release' endpoint: https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28
    # Find the 'tag_name' of the latest release and ensure that it follows a semantic version label
    # For example v1.0.0 -> x.y.z

    # Add new bool column for versioning format
    repos['semantic_versioning'] = ''

    for idx, row in enumerate(repos.to_dict(orient='records')):
        # print(row)
        releases_request = f"https://api.github.com/repos/{row['full_name']}/releases?page=1&per_page=1"
        print(releases_request)
        result = requests.get(releases_request, auth=(os.environ.get('username'),
                                                      os.environ.get('gh_token'))).json()
        if('message' in result):
            print(result)
            break

        if(len(result) == 0):
            repos.at[idx, 'semantic_versioning'] = False

        else:
            release = result[0]
            if ('tag_name' in release):
                # Clean tag name
                tag_name = str.casefold(release['tag_name'])
                if(tag_name.startswith('v')):
                    tag_name = tag_name[1:]

                # Check if semantic version
                sem_re = "^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
                if(re.search(sem_re, tag_name)):
                    repos.at[idx, 'semantic_versioning'] = True
                else:
                    repos.at[idx, 'semantic_versioning'] = False

    print(repos[['repository_ID', 'full_name', 'number_of_stars', 'semantic_versioning']])

    # Remove all non-semantically versioned repos
    # There seems to be a problem with semantic versions being assigned to dropped repos
    # Is there a way to delete the dropped rows? Or maybe my regex query considers a null value a semantic version?
    repos = repos.drop(repos[repos.semantic_versioning == False].index)
    print(repos[['repository_ID', 'full_name', 'number_of_stars', 'semantic_versioning']])


if __name__ == "__main__":
    main()


# Save those repositories to a new database or however you wish to store them
# You should now have a list of repos with less than 40k stars and semantic versioning
# We can make this list of repos smaller to fit the github API limit or for time constraints

# For each of these repos save all of the 'stargazer' instances with the 'starred at' property
# This gives a list of every user that has starred the repo and at what time/date they starred it
# Save this list for each repo

# For each of the repos use the 'Release' endpoint to identify major and minor releases
# So any changes to the x or y value in x.y.z
# For each of these releases, there is a 'created_at' value, note the date of every release.

# Finally, for every release, take the 'created_at' date and 1 week ahead of that 'created_at date'
# and count the number of stars that fall between the two dates
# this gives you the number of stars for each release.
# sum up the number of stars for every release to get number of stars following releases for a repo

# 1st graph is number of stars after a release/total number of stars
# (boxplot, 1 is stars for major releases 1 is stars for major and minor releases)

# 2nd graph number of stars after a release/fraction of weeks representing the total lifetime of the repo
