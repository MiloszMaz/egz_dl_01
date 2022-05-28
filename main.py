import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def funkcja(x):
    return (4-x+x**3)/(6+x-4*x**2+x**3)

def zadanie1():
    plt.axhline(y=0.5, color='r', linestyle='--')
    plt.axvline(x=-1, color='r', linestyle='--')
    plt.axvline(x=2, color='r', linestyle='--')
    plt.axvline(x=3, color='r', linestyle='--')

    x1 = np.linspace(-3, -1, 1000)
    y1 = funkcja(x1)
    plt.plot(x1, y1, color='b')

    x2 = np.linspace(-1, 2, 1000)
    y2 = funkcja(x2)
    plt.plot(x2, y2, color='b')

    x3 = np.linspace(2, 3, 1000)
    y3 = funkcja(x3)
    plt.plot(x3, y3, color='b')

    x4 = np.linspace(3, 5, 1000)
    y4 = funkcja(x4)
    plt.plot(x4, y4, color='b')

    plt.ylim(-50, 40)
    plt.xlim(-3, 5)

    plt.annotate('154749', xy=(1, 0), xycoords='axes fraction', horizontalalignment='left', verticalalignment='top')

    plt.show()

def zadanie11():
    values = [21, 27, 33, 15, 35]
    indexes = ['A', 'B', 'C', 'D', 'E']

    s = pd.Series(values, index=indexes)

    s.plot(kind='pie',
           fontsize=12,
           figsize=(6, 6),
           colors=['#d82647', '#2af6ea', '#af768a', '#a2d1ef', '#7c1b53'],
           title='Tytuł',
           ylabel='',
           labels=values,
           counterclock=True,
           startangle=90)

    plt.legend(loc='upper left', labels=indexes)
    plt.savefig('./zadanie1.pdf')

def zadanie2():
    xlsx = pd.ExcelFile('2020-e01/ceny.xlsx')
    df = pd.read_excel(xlsx, header=0)

    print(df.where(df['Rok'] == 2017).groupby('Rodzaje towarów i usług').mean())

    df.set_index('Miesiące', inplace=True)

    df.groupby('Rodzaje towarów i usług')['Wartosc'].plot(
        xlabel='Miesiąc',
        ylabel='Wartość',
        title='Wartość produktów w miesiącach'
    )

    plt.legend(loc='upper left')
    plt.savefig('2020-e01/zadanie2.jpg')


def zadanie3():
    df = pd.read_csv('2020-e01/gastro.csv', header=0, sep=';', decimal='.')
    df.set_index('Typy placówek', inplace=True)
    df = df.transpose()

    df = df.reset_index()
    df = df.rename_axis(None, axis=1)
    df = df.rename(columns={'index': 'Typy placówek'})

    df.pivot('Rok', 'Typy placówek', 'Wartosc').plot(
        kind='bar',
        xlabel='Lata',
        ylabel='Wartosc',
        rot=0,
        title='Wartość placówek')
    plt.show()

if __name__ == '__main__':

    #zadanie1()

    zadanie11()

    #zadanie2()

    #zadanie3()
