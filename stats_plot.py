import matplotlib
from pylab import *
import statistics
import datetime

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


#######stats_plot_2d_graph_series_plot
######### argument list given below, kindly follow the order in which the arguments are mentioned.
###########1. x_keys --> label for x axis.
###########2. y_keys --> label for y axis.
###########3. x_cordinate_data --> x_axis plot data.
###########4. y_cordinate_data --> y_axis plot data.



def stats_plot_2d_graph_series_plot(x_axis_key = [], y_axis_key = [], x_cordinate_values = [], y_cordinate_values = []):

    array_x = []
    array_y = []
    color_value = 0
    x_range_value = []
    y_range_value = []
    date_formatter = []
    unix_date_format = []
    year_format = []
    month_format = []
    day_format = []
    isdate = 0
    print len(x_cordinate_values.__getitem__(x_axis_key[0]))
    print len(y_cordinate_values.__getitem__(y_axis_key[0]))
    print len(x_axis_key)
    for k in range(len(x_axis_key)):
        x_range_value = x_cordinate_values.__getitem__(x_axis_key[k])
        y_range_value = y_cordinate_values.__getitem__(y_axis_key[k])

        for j in range(len(x_cordinate_values.__getitem__(x_axis_key[k]))):
            if '-' in x_range_value[j]:
                date_formatter = str(x_range_value[j]).split("u")
                date_formatter = str(date_formatter[1]).split("'")
                date_convert = datetime.datetime.strptime(date_formatter[1],'%Y-%m-%d')
                array_x.insert(k,date_convert)
                plot_date = []
                date_formatter = []
                array_y.insert(k,float(y_range_value[j]))
            elif '-' in y_range_value[j]:
                print "ooppsie dates on the y-axis not recommended, kindly align your data"
                sys.exit()
            else:
                array_x.insert(k,float(x_range_value[j]))
                array_y.insert(k,float(y_range_value[j]))
        if k == 0:
            if isdate == 1:
                plot_date(array_x,array_y)
            elif isdate == 2:
                plot_date(array_y,array_x)
            else:
                scatter(array_x,array_y)
           #plot(array_x,array_y,'bo')

        elif k == 1:
           plot(array_x,array_y,'ro')
        else:
           print "bye bye have a nice day"

        array_x = []
        array_y = []
        color_value = color_value.__int__() + 1
        #print len(array_x)


    show()


    #list_temp_x = []
    #list_temp_y = {}
    #for i in range(len(x_axis_key)):
    #    list_temp_x = str(array_x[i])
    #    float_temp_x = float(list_temp_x)
    #    print statistics.mean(float_temp_x)


    #print statistics.mean(array_x[0])

    #for i in range(len(array_x)):
    #    print array_x[i]

    #print statistics.mean(array_x)
    #statistics.mean(mean_x.__getitem__(x_axis_key[i]))
