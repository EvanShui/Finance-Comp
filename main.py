"""
This program compares stock data with historical articles
to determine if there's any correlation between certain
events, whether it be pertaining to the company's stock
or global, and a stock's price.
"""


import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Button
from yahoo_finance import Share
from datetime import date, timedelta,datetime
import holidays

stock = Share("atvi")
holiday = holidays.UnitedStates()
fig, ax = plt.subplots()


def month_calc(month_val, dateInp='none'):
    diff = 13 - month_val
    year_back = 0
    if date.today().month - month_val <= 0:
        year_back = 1
    if dateInp == 'month':
        return int(math.fabs(diff))
    if dateInp == 'year':
        return year_back

current_date = date.today().strftime("%Y-%m-%d")  # strftime converts date.today(), a datetime object, into a string since stock.get_historical only takes in strings
# string version of date.today()
five_days_ago = (date.today() - timedelta(5)).strftime("%Y-%m-%d")
week_ago = (date.today() - timedelta(7)).strftime("%Y-%m-%d")
month_ago = date.today().replace(month=month_calc(1, 'month'), year=date.today().year - month_calc(1, 'year')).strftime("%Y-%m-%d")
six_month_ago = date.today().replace(month=month_calc(6, 'month'), year=date.today().year - month_calc(6, 'year')).strftime("%Y-%m-%d")
year_ago = date.today().replace(year=date.today().year-1).strftime("%Y-%m-%d")
five_year_ago = date.today().replace(year=date.today().year-5).strftime("%Y-%m-%d")
ten_year_ago = date.today().replace(year=date.today().year-10).strftime("%Y-%m-%d")


def data_sort(data, val='none'):  #analyzes data. returns two lists, a list with dates and its corresponding stock values
    lst_val = []
    lst_date = []
    for i in data:
        for x in i:
            if x == 'Date':
                lst_date.append(datetime.strptime(i[x], "%Y-%m-%d").date())
            if x == 'Adj_Close':
                lst_val.append(i[x])
    return lst_val, lst_date


def data_gather(time, value='none'): #gather data based off of the time. Will return a list of values, dates, or both.
    data = stock.get_historical(time, current_date)
    lst_value, lst_date = data_sort(data)
    for val, date in enumerate(lst_date):
        if date in holiday:
            print(date)
            lst_date.remove(date)
            lst_value.remove(lst_value[val])
    if value == 'value':
        return lst_value
    elif value == 'date':
        return lst_date
    else:
        return lst_value, lst_date


def picker(event):
    ind = event.ind
    print('onpick3 scatter:', ind)

xdata = data_gather(month_ago, 'date')
ydata = data_gather(month_ago, 'value')
plt.xlabel('date (Year-Month-Date)')
plt.ylabel('price (dollars)')
fig.autofmt_xdate()
fig.subplots_adjust(bottom=0.26)
fig.canvas.mpl_connect('pick_event', picker)
ax.plot(xdata, ydata, picker=True)


class Index(object):
    xdata = data_gather(month_ago, 'date')
    ydata = data_gather(month_ago, 'value')
    low_date = week_ago
    high_date = current_date
    low_value = ydata[0]
    high_value = sorted(ydata)[len(ydata)-1]

    def five_days_ago(self, event):
        ax.clear()
        self.xdata = data_gather(five_days_ago, 'date')
        self.ydata = data_gather(five_days_ago, 'value')
        self.low_date = self.xdata[len(self.ydata) - 1]
        self.high_date = self.xdata[0]
        self.low_value = self.ydata[0]
        self.high_value = sorted(self.ydata)[len(self.ydata) - 1]
        print(self.low_date, self.high_date, self.low_value, self.high_value)
        fig.autofmt_xdate()
        ax.plot(self.xdata, self.ydata)
        ax.plot_date(self.xdata, self.ydata)
        fig.autofmt_xdate()
        fig.subplots_adjust(bottom=0.26)
        print(self.low_date)

    def month(self, event):
        ax.clear()
        self.xdata = data_gather(month_ago, 'date')
        self.ydata = data_gather(month_ago, 'value')
        self.low_date = self.xdata[len(self.ydata) - 1]
        self.high_date = self.xdata[0]
        self.low_value = self.ydata[0]
        self.high_value = sorted(self.ydata)[len(self.ydata) - 1]
        print(self.low_date, self.high_date, self.low_value, self.high_value)
        fig.autofmt_xdate()
        ax.plot(self.xdata, self.ydata)
        ax.plot_date(self.xdata, self.ydata)
        fig.autofmt_xdate()
        fig.subplots_adjust(bottom=0.26)
        print(self.low_date)


    def six_month(self, event):
        ax.clear()
        self.xdata = data_gather(six_month_ago, 'date')
        self.ydata = data_gather(six_month_ago, 'value')
        self.low_date = self.xdata[len(self.ydata) - 1]
        self.high_date = self.xdata[0]
        self.low_value = self.ydata[0]
        self.high_value = sorted(self.ydata)[len(self.ydata) - 1]
        print(self.low_date, self.high_date, self.low_value, self.high_value)
        fig.autofmt_xdate()
        ax.plot(self.xdata, self.ydata)
        ax.plot_date(self.xdata, self.ydata)
        fig.autofmt_xdate()
        fig.subplots_adjust(bottom=0.26)
        print(self.low_date)

    def one_year(self, event):
        ax.clear()
        self.xdata = data_gather(year_ago, 'date')
        self.ydata = data_gather(year_ago, 'value')
        self.low_date = self.xdata[len(self.ydata) - 1]
        self.high_date = self.xdata[0]
        self.low_value = self.ydata[0]
        self.high_value = sorted(self.ydata)[len(self.ydata) - 1]
        print(self.low_date, self.high_date, self.low_value, self.high_value)
        fig.autofmt_xdate()
        ax.plot(self.xdata, self.ydata)
        ax.plot_date(self.xdata, self.ydata, picker=True)
        fig.autofmt_xdate()
        fig.subplots_adjust(bottom=0.26)
        print(self.low_date)

    def five_year(self, event):
        ax.clear()
        self.xdata = data_gather(five_year_ago, 'date')
        self.ydata = data_gather(five_year_ago, 'value')
        self.low_date = self.xdata[len(self.ydata) - 1]
        self.high_date = self.xdata[0]
        self.low_value = self.ydata[0]
        self.high_value = sorted(self.ydata)[len(self.ydata) - 1]
        print(self.low_date, self.high_date, self.low_value, self.high_value)
        fig.autofmt_xdate()
        ax.plot(self.xdata, self.ydata)
        ax.plot_date(self.xdata, self.ydata, picker=True)
        fig.autofmt_xdate()
        fig.subplots_adjust(bottom=0.26)
        print(self.low_date)

    def refresh(self,event):
        self.axes.set_ylim()


callback = Index()
axMonth = plt.axes([0.81, 0.05, 0.1, 0.075])
axSixMonth = plt.axes([0.7, 0.05, 0.1, 0.075])  # button placement
axYear = plt.axes([0.59, 0.05, 0.1, 0.075])
ax_five_year = plt.axes([0.48, 0.05, 0.1, 0.075])

bMonth = Button(axMonth, '1 month')
bMonth.on_clicked(callback.month)
bSixMonth = Button(axSixMonth, '6 month')
bSixMonth.on_clicked(callback.six_month)
bYear = Button(axYear, '1 year')
bYear.on_clicked(callback.one_year)
bFiveYear = Button(ax_five_year, '5 years')
bFiveYear.on_clicked(callback.five_year)
plt.show()

#this program works now
