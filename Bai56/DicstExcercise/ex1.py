# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# def sort_dict_by_value(dicts):
# 	import operator
# 	return sorted(dicts.items(), key=operator.itemgetter(0))
# 	# sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
# print sort_dict_by_value(d)
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)