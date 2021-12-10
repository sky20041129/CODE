from datetime import datetime
import tkinter as tk
import os
import sys
import tkinter.font as tkFont


'''
This tool is for date and time calculator

'''

def raid_log():


    filepath="C:/timegap.txt"
    if os.path.exists(filepath):
        os.remove(filepath)


    with open(r'C:/SeinoLog.txt') as f:

        # for txt log
        with open("C:/timegap.txt", "w") as file:

            for line  in f:

#-------------------------------------------------------------------------------------------------
            #Add drive was started.
                if "started" in line:
                    x = (line[3:22].rstrip())
                    #print("start",x)
                    xx = (line.rstrip())
                    print(xx)

                    # for txt log
                    print(xx, file=file, sep='\n')

                if "completed" in line:
                    y = (line[3:22].rstrip())
                    #print("completed", y)
                    yy = (line.rstrip())
                    print(yy)

                    # for txt log
                    print(yy, file=file, sep='\n')

                    timex = datetime.strptime(x, "%Y/%m/%d %H:%M:%S")

                    timey = datetime.strptime(y, "%Y/%m/%d %H:%M:%S")

                    if timey > timex:
                        gap = timey - timex
                        print("-----------------------------------------------------------------------------Time gap:",gap)

                        #for txt log
                        print("-----------------------------------------------------------------------------Time gap:",gap, file=file)


                    else:
                        gap = timex - timey
                        print("-----------------------------------------------------------------------------Time gap:",gap)
                        
                        #for txt log
                        print("-----------------------------------------------------------------------------Time gap:",gap, file=file)


raid_log()
os.system("pause")
