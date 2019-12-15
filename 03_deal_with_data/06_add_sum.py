ret = sum([1, 2, 3, 1048])
print(ret)

import operator
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 1048]))
print(reduce(operator.add, [1, 2, 3, 4], 1))