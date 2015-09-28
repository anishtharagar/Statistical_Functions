import sys
from fnmatch import  *


##########stats_parser function takes 2 arguments
########### arguments listed below
#--> 1 . data_parser_type --> type of data to be parsed at this moment only value supported is 2d_graph
#--> 2.  python list  passed as an argument, this is the data which needs to be parsed.

def stats_parser (*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '2':
        print "List of arguments passed does not match the data type %.3d" % count_arg_length
        sys.exit()

    data_parser_type = args.__getitem__(0).__str__()
    data_list = args.__getitem__(1)

    if data_parser_type == '2d_graph':
        data_sample = {}
        key = []

        x_axis_data_points = []
        y_axis_data_points = []

        for i in range(len(data_list)):
            data_sample = (dict(data_list[i]))
            key = data_sample.keys()
            if key[0] == 'x':
                x_axis_data_points.append(data_sample.values())
            elif key[0] == 'y':
                y_axis_data_points.append(data_sample.values())

        x_list_collection = str(x_axis_data_points.__getitem__(0)).split(",")
        y_list_collection = str(y_axis_data_points.__getitem__(0)).split(",")
        x_temp = []
        y_temp = []

        for i in range(len(x_list_collection)):
            if '[' in x_list_collection[i]:
                print "gameon for ["
                x_temp = str(x_list_collection.__getitem__(i)).split("[")
                y_temp = str(y_list_collection.__getitem__(i)).split("[")
        for i in range(len(x_list_collection)):
            if '[' in x_list_collection[i]:
                print "skipping for data alignment"
            else:
                x_temp.append(str(x_list_collection.__getitem__(i)))
                y_temp.append(str(y_list_collection.__getitem__(i)))
        x_list_collection = []
        y_list_collection = []
        for i in range(len(x_temp)):
            if ']' in x_temp[i]:
                print "gameon for ]"
                x_list_collection = str(x_temp.__getitem__(i)).split("]")
                y_list_collection = str(y_temp.__getitem__(i)).split("]")
        x2_temp = []
        y2_temp = []
        for i in range (len(x_temp)):
            if ']' in x_temp[i]:
                print "skipping for data alignment"
            elif 'u' in x_temp[i]:
                print "skipping for data alignment"
            else:
                x2_temp.append(str(x_temp.__getitem__(i)))
                y2_temp.append(str(y_temp.__getitem__(i)))
        x2_temp.append(str(x_list_collection.__getitem__(0)))
        y2_temp.append(str(y_list_collection.__getitem__(0)))

        x_axis_data_points = []
        y_axis_data_points = []
        x_axis_data_points = x2_temp
        y_axis_data_points = y2_temp
        print x_axis_data_points
        print y_axis_data_points
        return x_axis_data_points, y_axis_data_points
    else:
        print "Data parser type not supported"
        sys.exit()


