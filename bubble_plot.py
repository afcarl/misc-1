import csv
from urllib2 import urlopen
from itertools import islice
from pylab import axis, figure, scatter, show, sqrt, text, xlabel, ylabel
import pandas

def plot_without_pandas():

    x, y, color, area, names = [], [], [], [], []

    for row in islice(csv.reader(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv')), 2, None):

        # fields are state, murder, forcible_rape, robbery, aggravated_assault, burglary, larceny_theft, motor_vehicle_theft, population

        x.append(float(row[1])) # murder
        y.append(float(row[5])) # burglary

        color.append(float(row[6])) # larceny
        area.append(sqrt(int(row[8]))) # population

        names.append(row[0]) # state

        text(row[1], row[5], row[0], size=11, horizontalalignment='center')

    sct = scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')

    sct.set_alpha(0.75)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    xlabel('Murders per 100,000 population')
    ylabel('Burglaries per 100,000 population')

    show()

def draw_simple_text(row):

    text(row['murder'], row['burglary'], row['state'], size=11, horizontalalignment='center')

def plot_with_pandas():

    data = pandas.read_csv(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv'), skiprows=[1])

    data.apply(draw_simple_text, axis=1)

    sct = scatter(data['murder'], data['burglary'], c=data['larceny_theft'], s=sqrt(data['population']), linewidths=2, edgecolor='w')

    sct.set_alpha(0.75)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    xlabel('Murders per 100,000 population')
    ylabel('Burglaries per 100,000 population')

    show()

def draw_text(row, scale, min_population):

    text(row['murder'], row['burglary'], row['state'], size=((row['population'] - min_population) / scale + 8), horizontalalignment='center')

def text_plot_with_pandas():

    data = pandas.read_csv(urlopen('http://datasets.flowingdata.com/crimeRatesByState2005.csv'), skiprows=[1])

    min_population = min(data['population'])

    scale = (max(data['population']) - min_population) / 20.0

    ax = figure().add_subplot(111)

    data.apply(draw_text, args=(scale, min_population), axis=1)

    axis([0, 11, 200, 1280]) # DC is an outlier!

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    show()

if __name__ == '__main__':

    #plot_with_pandas()
    plot_without_pandas()
    #text_plot_with_pandas()