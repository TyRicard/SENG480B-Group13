import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def main():
    # https://www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    percent_stars = pd.read_csv("../data/datasets/RQ3_data.csv")

    # This produces an ECDF plot
    ecdf_plot =  sns.ecdfplot(data=percent_stars.filter(like="percent_", axis="columns"))

    # Changing the Label Titles to Match Approach
    ecdf_plot.set(xlabel="Fraction of Time Since Create",
                  ylabel="Prob (Fraction of Time Since Create)",
                  xlim = (0.0, 1.0),
                  ylim = (0.0, 1.0))

    plt.show()

if __name__ == "__main__":
    main()