import sys


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
                x_axis_data_points.extend(data_sample.values())
            elif key[0] == 'y':
                y_axis_data_points.extend(data_sample.values())

        return x_axis_data_points, y_axis_data_points
    else:
        print "Data parser type not supported"
        sys.exit()




