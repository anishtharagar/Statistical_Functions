from scipy import stats
import numpy
import statistics
import pymongo
import mongo_connect

mongo = pymongo.Connection('127.0.0.1')
mongo_db = mongo ['raw_data']
mongo_collections = mongo_db['congruent_values']
mongo_collections2 = mongo_db['incongruent_values']


congruent_sample_data = [12.079,16.791,9.564,8.63,14.669,12.238,14.692,8.987,9.401,14.48,22.328,15.298,15.073,16.929,18.2,12.13,18.495,10.639,11.344,12.369,12.944,14.233,19.71,16.004]
incongruent_sample_data = [19.278,18.741,21.214,15.687,22.803,20.878,24.572,17.394,20.762,26.282,24.524,18.644,17.51,20.33,35.255,22.158,25.139,20.429,17.425,34.288,23.894,17.96,22.058,21.157]

array=numpy.linspace(12.01,16.99,num=3)
keys = ['x','y']

data_payload_congruent = {}
data_payload_incongruent = {}
k=1

for i in array:
    congruent_sample = stats.ttest_1samp(congruent_sample_data, i)
    print "The t-statistic is %.3f and the p-value is %.3f." % congruent_sample
    incongruent_sample = stats.ttest_1samp(incongruent_sample_data, i+8)
    print "The t-statistic is %.3f and the p-value is %.3f." % incongruent_sample

    for j in range(len(keys)):
        data_payload_congruent.__setitem__(keys.__getitem__(j).__str__()+k.__str__(),congruent_sample.__getitem__(j).__str__())


    for j in range(len(keys)):
        data_payload_incongruent.__setitem__(keys.__getitem__(j).__str__()+k.__str__(),incongruent_sample.__getitem__(j).__str__())

    k = k.__int__() + 1

mongo_connect.mongo_delete_load('127.0.0.1','raw_data','congruent','join',data_payload_congruent)
mongo_connect.mongo_delete_load('127.0.0.1','raw_data','incongruent','join',data_payload_incongruent)

print "Congruent sample standard deviation %.3f." % statistics.stdev(congruent_sample_data)
print "InCongruent sample standard deviation %.3f." % statistics.stdev(incongruent_sample_data)

print "Mean value for Congruent dataset : %.3f." % statistics.mean(congruent_sample_data)
print "Mean value for Incongruent dataset : %.3f." % statistics.mean(incongruent_sample_data)

print "Median Value for congruent dataset : %.3f."% statistics.median(congruent_sample_data)
print "Median Value for incongruent dataset : %.3f."% statistics.median(incongruent_sample_data)


