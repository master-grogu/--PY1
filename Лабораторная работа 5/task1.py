# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list1 = [{'dec': _, 'bin': bin(_), 'oct': oct(_), 'hex': hex(_)} for _ in range(16)]
pprint(list1)
