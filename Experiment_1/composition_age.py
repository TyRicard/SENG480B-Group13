import datetime as dt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This file was copied mainly from Experiment 2 with modifications to get a boxplot
# Adding Custom Mapping Function
def subtract_times(past_str):
    # For Datetime Calculations: https://docs.python.org/3/library/datetime.html
    # This current_time is technically variable but the program runs fast enough
    # that the only change for incorrect results is if the value is taken at midnight
    current_time = dt.datetime.now()
    past_time = dt.datetime.strptime(past_str, '%Y-%m-%d %H:%M:%S')
    difference = current_time - past_time
    # Use floor division
    return (difference.days // 7)


def main():
    # Basic Seaborn Approach: https://seaborn.pydata.org/tutorial/introduction
    repo_df = pd.read_csv("../data/datasets/data.csv")

    # For element-wise Calculation with Pandas: https://queirozf.com/entries/pandas-dataframe-examples-column-operations
    repo_df["age"] = repo_df['created_date'].map(lambda cd: subtract_times(cd))
    # This produces a boxplot
    boxplot =  sns.boxplot(
                    data=repo_df,
                    y="age")

    # Changing the Label Titles to Match Approach
    boxplot.set(ylabel="Age (Weeks)")

    plt.show()

if __name__ == "__main__":
    main()