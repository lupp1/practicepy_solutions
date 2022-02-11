# Birthday Plots www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html
# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
# Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. 
# Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

from bokeh.plotting import figure, show, output_file
from birthday_months import main
from birthday_months import months


output_file("plot.html")
x_categories = [month for month in months.keys()]
x = [m for m in main().keys()]
y = [count for count in main().values()]

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)


