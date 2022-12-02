# Read in data from from datasets/data.csv
# Loop through each repo, remove any repo with more than 40000 stars

# For every remaining repo
# Use the 'Release' endpoint: https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28
# Find the 'tag_name' of the latest release and ensure that it follows a semantic version label
# For example v1.0.0 -> x.y.z

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
