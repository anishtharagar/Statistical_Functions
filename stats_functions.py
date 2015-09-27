from scipy import stats
import statistics
import pymongo
import mongo_connect

def stat_functions_usage(mongo_host,mongo_db_name,mongo_collection_name = [],functions = [],query = []):

        return_data = mongo_connect.mongo_collect_data(mongo_host,mongo_db_name,mongo_collection_name)
        #return_data = mongo_connect.mongo_query_data(mongo_host,mongo_db_name,mongo_collection_name,query)

        data_sample = {}
        key = []
        x_axis_data_points = []
        y_axis_data_points = []
        for i in range(len(return_data)):
            data_sample = (dict(return_data[i]))
            key = data_sample.keys()
            if key[0] == 'x':
                x_axis_data_points.extend(data_sample.values())
            elif key[0] == 'y':
                y_axis_data_points.extend(data_sample.values())

        print x_axis_data_points[0]
        print y_axis_data_points[0]


stat_functions_usage('127.0.0.1','raw_data',["graph_congruent_incongruent"])

