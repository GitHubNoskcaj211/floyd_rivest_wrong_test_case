from quickselect import floyd_rivest
import pickle
from copy import deepcopy

values = pickle.load(open('test.pkl', 'rb'))
N = 10

values1 = deepcopy(values)
output1 = sorted(values1, reverse=True)
if N is not None:
    output1 = output1[:N]
print(output1)

values2 = deepcopy(values)
nth_largest_score = floyd_rivest.nth_largest(values2, N - 1)
print(nth_largest_score)
output2 = [value for value in values2 if value >= nth_largest_score]
output2 = sorted(output2, reverse=True)
print(output2)