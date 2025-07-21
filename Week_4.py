# Finding the Maximum and Minimum Numbers from a List"
import sys

listA= [ 23, 12, 45, 22, 11, 78, 13, 90, 45, 88, 10, -5, -1 ]
max_int = -sys.maxsize
min_int = sys.maxsize

for i in listA :
    max_int = i if max_int < i else max_int
    min_int = i if i < min_int else min_int

print(f"Max val: {max_int}")
print(f"Min val: {min_int}")