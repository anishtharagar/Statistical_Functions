import matplotlib
from pylab import *
import statistics

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

    mean_x = mean(x_range_values)
    mean_y = mean(y_range_values)
    median_x = median(x_range_values)
    median_y = median(y_range_values)
    median_group_x = statistics.median_grouped(x_range_values)
    median_group_y = statistics.median_grouped(y_range_values)
    print x_range_values
    print y_range_values
    p_variance_value_x = statistics.pvariance(x_range_values)
    p_variance_value_y = statistics.pvariance(y_range_values)
    xlabel(x_label)
    ylabel(y_label)
    plot(x_range_values,y_range_values,'ro')
    text(mean_x,mean_y,"<-- That's the mean value of x and y")
    text(median_group_x,median_group_y,"<-- Median Group value of x and y after interpolation")

    x_range_values.sort()
    y_range_values.sort()
    x_range_values.reverse()
    y_range_values.reverse()
    value_for_graph_info_xlabels = x_range_values[0] - 2
    value_for_graph_info_ylabels = y_range_values[0] + 2
    text(value_for_graph_info_xlabels,value_for_graph_info_ylabels,"Pvariance_x --> %.3d"% p_variance_value_x)
    value_for_graph_info_ylabels = value_for_graph_info_ylabels - 1
    text(value_for_graph_info_xlabels,value_for_graph_info_ylabels,"Pvariance_y --> %.3d"% p_variance_value_y)
    value_for_graph_info_ylabels = value_for_graph_info_ylabels + 2
    text(value_for_graph_info_xlabels,value_for_graph_info_ylabels,"Mean_x  --> %.3d"% mean_x)
    value_for_graph_info_ylabels = value_for_graph_info_ylabels + 1
    text(value_for_graph_info_xlabels,value_for_graph_info_ylabels,"Mean_y  --> %.3d"% mean_y)
    show()



