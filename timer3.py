"""
Python Timer3 Module
-----------------------
Create and set timers with this module.
"""

import time
stopped = True
__author__ = "ValidIdiot"
__copyright__ = "Copyright 2022, ValidIdiot"
__credits__ = "ValidIdiot"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "ValidIdiot"
__email__ = "valididotexists@gmail.com"

class Timer():
    print("Thanks for using Timer3 " + __version__ + "!")
    def __init__(self):
        pass
    def start_timer(duration: int, showing: bool):
        """
        Start Timer
        ---------------
        This function is self explantory. It starts a timer!
        
        WARNING! Timer only supports seconds.
        >>> def start_timer(duration: int, showing: bool):
        """
        stopped = False
        global timer
        timer = 0
        while stopped == False:
            time.sleep(1)
            timer += 1
            duration -= 1
            if showing == True:
                print(timer)
            else:
                pass
            if duration <= 0:
                stopped = True
                print("Timer stopped.")