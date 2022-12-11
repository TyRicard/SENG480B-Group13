import pandas
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pandas.read_csv('../data/datasets/data.csv')
    df = df.drop(df.iloc[:, :9], axis=1)
    df = df.drop(df.iloc[:, 2:], axis=1)
    df = df.dropna()

    plot = pandas.DataFrame({col: vals['number_of_stars'] for col, vals in df.groupby(by=['type'])})
    med = plot.median().sort_values(ascending=False)
    box = plot[med.index].boxplot(rot=15, figsize=(10, 10), showfliers=False)

    plt.show()