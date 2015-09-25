import sys
import os
import thread
import threading

import time

class threadex(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,None):
            self.exit=False
            self.name=name
            self.start()
            self.done=0
            self.sum=0

    def run(self):
        while True:
            continue
