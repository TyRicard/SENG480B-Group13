import pandas
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pandas.read_csv('data.csv')
    df = df.drop(df.iloc[:, :6], axis=1)
    df = df.drop(df.iloc[:, 2:], axis=1)
    print(df)
    top10 = df
    top10 = top10.dropna()
    top10 = top10.groupby(['Language'])['number_of_stars'].count()
    top10 = top10.sort_values(ascending=False)
    top10 = top10.iloc[:10]
    top10 = top10.to_frame()
    top10 = top10.index.values

    df = df[df.Language.isin(top10) == True]

    topMedian = df.groupby(['Language'])['number_of_stars'].median()
    topMedian = topMedian.sort_values(ascending=False)
    print(topMedian)

    plot = pandas.DataFrame({col: vals['number_of_stars'] for col, vals in df.groupby(by=['Language'])})
    med = plot.median().sort_values(ascending=False)
    box = plot[med.index].boxplot(rot=15, figsize=(10, 10), showfliers=False)

    plt.show()
