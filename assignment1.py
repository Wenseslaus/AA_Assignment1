import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    pairs=0
    for val in Counter(ar).values():
        pairs+=val//2
    return pairs

n = 7
array = arr=[1,2,1,1,2,1,3,2]
print(sockMerchant(n, array))
