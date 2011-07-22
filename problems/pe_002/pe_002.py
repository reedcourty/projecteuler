#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Answer: 4613732

import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, root_dir)

import runlikehell as rh

s = rh.Stopper()
s.start()

LIMIT = 4000000
list = [1,2]
i=0
sum=0

while list[len(list)-1] < LIMIT:
    list.append(list[i]+list[i+1])
    i = i + 1
   
for i in list:
    if (i % 2 == 0):
        sum=sum+i

print(sum)

s.stop()

print("running time: " + s.get_result()) 
