#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

class Stopper():
    def __init__(self):
        pass
        
    def start(self):
        self.now = datetime.datetime.now()
        
    def stop(self):
        self.result = datetime.datetime.now() - self.now
        
    def get_result(self):
        return str(self.result.total_seconds())