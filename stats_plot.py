import matplotlib
from pylab import *

#######stats_plot_2d_graph
######### argument list given below, kindly follow the order in which the arguments are mentioned.
###########1. x_label --> label for x axis.
###########2. y_label --> label for y axis.
###########3. x_cordinate_data --> x_axis plot data.
###########4. y_cordinate_data --> y_axis plot data.
def stats_plot_2d_graph(x_label, y_label, x_cordinate_data = [],y_cordinate_data = []):


    #map(float,x_cordinate_data)
    #map(float,y_cordinate_data)
    x_range_values = []
    y_range_values = []
    j=0
    for i in range (len (x_cordinate_data)):
        if i == 0:
            print "skipping for error round off"
        else:
            x_range_values.insert(j,float(x_cordinate_data[i]))
            y_range_values.insert(j,float(y_cordinate_data[i]))
            j=j.__int__()+1

    xlabel(x_label)
    ylabel(y_label)
    plot(x_range_values,y_range_values)
    show()



