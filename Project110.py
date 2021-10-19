import pandas as pd
import random 
import plotly.figure_factory as ff 
import statistics

lists =pd.read_csv('medium_data.csv')

population = lists['reading_time'].to_list()

population_mean = statistics.mean(population)

def random_set_of_mean(UL) : 
    dataset = []
    for i in range(0,UL) : 
        random_index = random.randint(0,len(population)-1)
        value = population[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup() : 
    mean_list = []
    for i in range(0,100) : 
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    sample_mean_value = statistics.mean(mean_list)
    show_fig(mean_list)

    print('')
    print('The actual mean of the population is :- {}'.format(population_mean))
    print('The sampling mean of the population is :- {}'.format(sample_mean_value))
    print('')

def show_fig(mean_list) :
    fig = ff.create_distplot([mean_list] , ["Population"] , show_hist = False)
    fig.show()

setup()
