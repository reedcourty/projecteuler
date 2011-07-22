#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Answer: 233168

import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, root_dir)

import runlikehell as rh

LIMIT = 1000

s = rh.Stopper()
s.start()
sum = 0
for i in range(0, LIMIT):
    if ((i % 3)==0) or ((i % 5)==0):
        sum=sum+i
print(sum)
s.stop()

print("running time: " + s.get_result()) 


