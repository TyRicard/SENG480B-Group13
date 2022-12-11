import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    stars_and_topics = pd.read_csv("../data/datasets/data.csv")

    # This produces a barplot
    bar_plot =  sns.barplot(
                    data=stars_and_topics,
                    x="topics_count",
                    y="number_of_stars")

    # Changing the Label Titles to Match Approach
    bar_plot.set(xlabel="Topics Count",
                    ylabel="Stars",
                    yscale="log",
                    ylim=10000)

    plt.show()

if __name__ == "__main__":
    main()
