import datetime as dt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    stars_and_age = pd.read_csv("../data/datasets/data.csv")

    # For element-wise Calculation with Pandas: https://queirozf.com/entries/pandas-dataframe-examples-column-operations
    stars_and_age["age"] = stars_and_age['created_date'].map(lambda cd: subtract_times(cd))
    # This produces a scatterplot
    scatter_plot =  sns.scatterplot(
                    data=stars_and_age,
                    x="age",
                    y="number_of_stars")

    # Changing the Label Titles to Match Approach
    scatter_plot.set(xlabel="Age (Weeks)",
                    ylabel="Stars",
                    yscale="log",
                    ylim=1000)

    plt.show()

if __name__ == "__main__":
    main()