import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This file was copied mainly from Experiment 2 with modifications to get a boxplot
# The graph is accurate and Linux is an extreme outlier
def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    repo_df = pd.read_csv("../data/datasets/data.csv")

    # This produces a boxplot without outliers
    boxplot = sns.boxplot (
                    data=repo_df,
                    y="commit_count",
                    showfliers=False)

    # Changing the Label Titles to Match Approach
    boxplot.set(ylabel="Commits")

    plt.show()

if __name__ == "__main__":
    main()