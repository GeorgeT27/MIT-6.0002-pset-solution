# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

from cProfile import label
from statistics import mean
from numpy import average
import numpy
import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    coe=[]
    for deg in degs:
        model_coe=pylab.polyfit(x,y,deg)
        coe.append(model_coe)
    return coe


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    Error_in_estimate=((y-estimated)**2).sum()
    Variability_in_measured_data=((y-y.mean())**2).sum()
    Rsqr=1-Error_in_estimate/Variability_in_measured_data
    return Rsqr
    

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    
    for model in models:
        yest=pylab.polyval(model,x)
        pylab.figure()
        pylab.plot(x,y,"bo",label="Data Point")
        pylab.plot(x,yest,"r-",label="model")
        pylab.legend(loc="best")
        if len(model)==2:
            pylab.title(f"The degree of the regression model is {len(model)-1} \n R_squared={r_squared(y,yest)} \n SE/slope={se_over_slope(x,y,yest,model)}")
        else:
            pylab.title(f"The degree of the regression model is {len(model)-1} \n R_squared={r_squared(y,yest)}")
        pylab.xlabel('Year')
        pylab.ylabel('Temperature in Celsius')
        pylab.show()

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    # annual_temp=[]
    # for year in years:
    #     city_temp=[]
    #     for city in multi_cities:
    #         city_temp.append(climate.get_yearly_temp(city,year))
    #     annual_temp.append(mean(city_temp))
    # return pylab.array(annual_temp)
    
    multi_temperature_avg = []
    for year in years:
        yearly_temperature = []
        for city in multi_cities:
            yearly_temperature.append(climate.get_yearly_temp(city, year))
        yearly_temperature = pylab.array(yearly_temperature)   # converting list to an array.
        multi_temperature_avg.append(yearly_temperature.mean())
    multi_temperature_avg = pylab.array(multi_temperature_avg) # converting list to an array.
    return multi_temperature_avg

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    moving_average=[]
    leny=len(y)
    num=1
    while num<=window_length:
        average=sum(y[0:num])/num
        moving_average.append(average)
        num+=1
    for i in range(leny-window_length):
        average=sum(y[1+i:1+i+window_length])/window_length
        moving_average.append(average)
    return pylab.array(moving_average)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    top=((y-estimated)**2).sum()
    RMSE=(top/len(y))**(1/2)
    return RMSE
    

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    annual_std_dev = []
    for year in years:
        all_cities_yearly_temp = []
        for city in multi_cities:
            year_data=climate.get_yearly_temp(city,year)
            all_cities_yearly_temp.append(year_data)
        all_cities_yearly_temp = pylab.array(all_cities_yearly_temp)   # converting list to an array.
        daily_mean = all_cities_yearly_temp.mean(axis=0) 
        std=numpy.std(daily_mean)
        annual_std_dev.append(std)
    return pylab.array(annual_std_dev)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        pylab.figure()
        pylab.plot(x,y,"bo",label="data point")
        yest=pylab.polyval(model,x)
        pylab.plot(x,yest,"r-",label="model")
        pylab.title(f"Degree of regrssion model:{len(model)-1} \n RMSE:{rmse(y,yest)}")
        pylab.legend(loc="best")
        pylab.xlabel('Year')
        pylab.ylabel('Temperature in Celsius')
        pylab.show()
        
    

if __name__ == '__main__':



    # Part A.4
    # data_file=Climate("data.csv")
    # tempt_list=[]
    # for year in TRAINING_INTERVAL:
    #     tempt=data_file.get_daily_temp("NEW YORK",1,10,year)
    #     tempt_list.append(tempt)
    # tempt_array=pylab.array(tempt_list)
    # coes=generate_models(pylab.array(TRAINING_INTERVAL),tempt_array,[1])
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),tempt_array,coes)
    
    # data_file=Climate("data.csv")
    # tempt_list=[]
    # for year in TRAINING_INTERVAL:
    #     temptlist=data_file.get_yearly_temp("NEW YORK",year)
    #     tmp_avg=average(temptlist)
    #     tempt_list.append(tmp_avg)
    # tempt_array=pylab.array(tempt_list)
    # coes2=generate_models(pylab.array(TRAINING_INTERVAL),tempt_array,[1])
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),tempt_array,coes2)

    
    # # Part B
    # year_avg=gen_cities_avg(data_file,CITIES,TRAINING_INTERVAL)
    # coes3=generate_models(pylab.array(TRAINING_INTERVAL),year_avg,[1])
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),pylab.array(year_avg),coes3)

    # # Part C
    # data_file = Climate('data.csv')
    # all_cities_avg = gen_cities_avg(data_file, CITIES, TRAINING_INTERVAL)
    # year_moving=moving_average(all_cities_avg,5)
    # coes4=generate_models(pylab.array(TRAINING_INTERVAL),year_moving,[1])
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),year_moving,coes4)

    # Part D.2
    # data_file = Climate('data.csv')
    # all_cities_avg = gen_cities_avg(data_file, CITIES, TRAINING_INTERVAL)
    # year_moving=moving_average(all_cities_avg,5)
    # coes5=generate_models(pylab.array(TRAINING_INTERVAL),year_moving,[1,2,20])
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),year_moving,coes5)
    
    # data_file=Climate("data.csv")
    # test_all_cities_avg=gen_cities_avg(data_file,CITIES,TESTING_INTERVAL)
    # test_year_moving=moving_average(test_all_cities_avg,5)
    # evaluate_models_on_testing(TESTING_INTERVAL,test_year_moving,coes5)

    # Part E
    data_file=Climate("data.csv")
    std=gen_std_devs(data_file,CITIES,pylab.array(TRAINING_INTERVAL))
    moving_avg_std=moving_average(std,5)
    coe6=generate_models(pylab.array(TRAINING_INTERVAL),moving_avg_std,[1])
    evaluate_models_on_training(pylab.array(TRAINING_INTERVAL),moving_avg_std,coe6)
