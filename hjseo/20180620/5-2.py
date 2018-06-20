#1
# 1. import - compare "__name__" variable whether "__main__" or not
# 2. append new module's path to sys module's "sys.path" variable
# 3. "PYTHONPATH" env variable setting

#2
import sys
sys.path.append("C:\\modules")


from mymod import mysum
print(mysum(1, 2))
