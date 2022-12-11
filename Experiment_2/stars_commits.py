import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    stars_and_commits = pd.read_csv("../data/datasets/data.csv")

    # This produces a scatterplot
    scatter_plot =  sns.scatterplot(
                    data=stars_and_commits,
                    x="commit_count",
                    y="number_of_stars")

    # Changing the Label Titles to Match Approach
    scatter_plot.set(xlabel="Commits",
                    ylabel="Stars",
                    xscale="log",
                    yscale="log",
                    ylim=10000)

    plt.show()

if __name__ == "__main__":
    main()