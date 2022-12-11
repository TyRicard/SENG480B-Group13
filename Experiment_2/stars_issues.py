import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    stars_and_issues = pd.read_csv("../data/datasets/data.csv")

    # This produces a scatterplot
    scatter_plot =  sns.scatterplot(
                    data=stars_and_issues,
                    x="issues_count",
                    y="number_of_stars")

    # Changing the Label Titles to Match Approach
    scatter_plot.set(xlabel="Issues Count",
                    ylabel="Stars",
                    yscale="log",
                    ylim=10000)

    plt.show()

if __name__ == "__main__":
    main()
