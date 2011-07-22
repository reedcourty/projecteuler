#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Answer: ????????

import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, root_dir)

import runlikehell as rh

s = rh.Stopper()
s.start()

#
#
# Problem solving comes here
#
#

s.stop()

print("running time: " + s.get_result()) 


