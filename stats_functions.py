from scipy import stats
import statistics
import pymongo
import mongo_connect
import stats_data_parser

def stat_functions_usage(mongo_host,mongo_db_name,mongo_collection_name = [],functions = [],query = []):


        return_data = mongo_connect.mongo_collect_data(mongo_host,mongo_db_name,mongo_collection_name)
        #return_data = mongo_connect.mongo_query_data(mongo_host,mongo_db_name,mongo_collection_name,query)

######

        x_axis_data_points, y_axis_data_points = stats_data_parser.stats_parser("2d_graph", return_data)
        print x_axis_data_points[0]
        print y_axis_data_points[0]



stat_functions_usage('127.0.0.1','raw_data',["graph_congruent_incongruent"])

