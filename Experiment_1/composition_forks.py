import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This was derived from the experiment two files
# Tensorflow appeared to be a massive outlier for this
def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    repos_df = pd.read_csv("../data/datasets/data.csv")

    # This produces a boxplot
    # To Remove Outliers: https://www.mikulskibartosz.name/how-to-remove-outliers-from-seaborn-boxplot-charts/
    boxplot =  sns.boxplot(
                    data=repos_df,
                    y="forks_count",
                    showfliers=False)

    # Changing the Label Titles to Match Approach
    boxplot.set(ylabel="Forks")

    plt.show()

if __name__ == "__main__":
    main()