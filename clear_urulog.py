from pathlib import Path
import os
def clear_log():
    my_file = Path("C:/Program Files (x86)/Universal RAID Utility/server/raid.log")
    if my_file.is_file():
        print ("Delete the uru log")
        os.remove(my_file)
        os.system("pause")
        # file exists
clear_log()
