import pandas
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pandas.read_csv('data.csv')
    df = df.drop(df.iloc[:, :6], axis=1)
    df = df.drop(df.iloc[:, 2:], axis=1)
    top10 = df
    top10 = top10.dropna()
    top10 = top10.groupby(['Language'])['number_of_stars'].count()
    top10 = top10.sort_values(ascending=False)
    top10 = top10.iloc[:10]
    top10 = top10.to_frame()
    temp = top10.index.values
    top10['Language'] = temp
    print(top10)


    plot = top10.plot.bar(x='Language', y='number_of_stars', rot=15, title='Top 10 Languages by star count')
    plt.show()