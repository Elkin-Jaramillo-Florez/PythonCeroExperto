import sys

# print(sys.path)

import re

text = "Mi numero de telefono es 3114568967 el codigo del pais es 57, mi numero de la suerte es el 3"
result = re.findall("[0-9]+", text)
print(result)


import time

timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)
print(result)

import collections

numbers = [12, 3, 2, 3, 3, 3, 5, 32, 32, 6, 7, 4, 7, 1, 12]
counter = collections.Counter(numbers)
print(counter)
