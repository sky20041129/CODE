from datetime import datetime
import tkinter as tk
import os
import sys
import tkinter.font as tkFont


'''
This tool is for date and time calculator

'''

def raid_log():
    with open(r'C:/Program Files (x86)/Universal RAID Utility/server/raid.log') as f:
        for line  in f:

#-------------------------------------------------------------------------------------------------
            # Consistency Check was started.

            if "Consistency Check was started." in line:
                x = (line[0:19].rstrip())
                #print("CC start",x)
            if "Consistency Check completed" in line:
                y = (line[0:19].rstrip())
                #print("CC completed",y)

                timex = datetime.strptime(x, "%Y/%m/%d,%H:%M:%S")

                timey = datetime.strptime(y, "%Y/%m/%d,%H:%M:%S")

                if timey > timex:
                    gap = timey - timex
                    print("CC gap" ,gap)

                else:
                    gap = timex - timey

                    print("CC gap",gap)
#-------------------------------------------------------------------------------------------------
            # Rebuild was started
            if "Rebuild was started." in line:
                x = (line[0:19].rstrip())
                #print("Rebuild start",x)

            if "Rebuild completed" in line:
                y= (line[0:19].rstrip())
                #print("Rebuild completed",y)

                timex = datetime.strptime(x, "%Y/%m/%d,%H:%M:%S")

                timey = datetime.strptime(y, "%Y/%m/%d,%H:%M:%S")

                if timey > timex:
                    gap = timey - timex
                    print("Rebuild gap" ,gap)

                else:
                    gap = timex - timey
                    print("Rebuild gap" ,gap)

#-------------------------------------------------------------------------------------------------
            #Initialization was started.
            if "Initialization was started." in line:
                x = (line[0:19].rstrip())
                #print("init start",x)

            if "Initialization completed." in line:
                y = (line[0:19].rstrip())
                #print("init completed",y)

                timex = datetime.strptime(x, "%Y/%m/%d,%H:%M:%S")

                timey = datetime.strptime(y, "%Y/%m/%d,%H:%M:%S")

                if timey > timex:
                    gap = timey - timex
                    print("init gap" ,gap)

                else:
                    gap = timex - timey
                    print("init" ,gap)
raid_log()
os.system("pause")
