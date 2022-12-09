import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# This file was copied mainly from Experiment 2 with modifications to get a boxplot
# Linux had too many contributors and DefinetlyTyped had the most as an outlier
# but its value was also off by 4000 due to the anonymous issue.

def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    repos_df = pd.read_csv("../data/datasets/data.csv")

    # This produces a boxplot without outliers
        # To Remove Outliers: https://www.mikulskibartosz.name/how-to-remove-outliers-from-seaborn-boxplot-charts/
    boxplot =  sns.boxplot(
                    data=repos_df,
                    y="contributor_count",
                    showfliers=False)

    # Changing the Label Titles to Match Approach
    boxplot.set(ylabel="Contributors")

    plt.show()

if __name__ == "__main__":
    main()