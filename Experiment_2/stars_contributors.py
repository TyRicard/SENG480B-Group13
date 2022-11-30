import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    stars_and_contributors = pd.read_csv("../data/datasets/data.csv")

    # This produces a scatterplot
    scatter_plot =  sns.scatterplot(
                    data=stars_and_contributors,
                    x="contributor_count",
                    y="number_of_stars")

    # Changing the Label Titles to Match Approach
    scatter_plot.set(xlabel="Contributors",
                    ylabel="Stars",
                    xscale="log",
                    yscale="log",
                    ylim=1000)

    plt.show()

if __name__ == "__main__":
    main()