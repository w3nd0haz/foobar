#!/usr/bin/env python
# sort list of files by its ctime
import sys
import os
import time

MRTG_CFG_DIR = '/mydirectory'
MRTG_CFG_FILENAME = 'interestingfile.txt'
DEF_LIST_LEN = 50 # number of items that must be returned
DEF_WAIT_INTERVAL = 2 # sleep before build the dictionary
DEF_MIN_AGE = 60 # minimum required file age

if __name__ == "__main__":
        count = 0
        fileList = {}
        currentTime = int(time.time())
        try:
                list_len = int(sys.argv[1])
                wait_interval = int(int(sys.argv[2]) * DEF_WAIT_INTERVAL)
                file_min_age = int(sys.argv[3])
        except:
                list_len = DEF_LIST_LEN
                wait_interval = 0
                file_min_age = DEF_MIN_AGE
        try:
                time.sleep(wait_interval)
                for a in os.listdir(MRTG_CFG_DIR):
                        if a != '.' and a != '..' and os.path.isdir(MRTG_CFG_DIR+'/'+a):
                                for m in os.listdir(MRTG_CFG_DIR+'/'+a):
                                        if m == MRTG_CFG_FILENAME:
                                                f_ctime = int(os.stat(MRTG_CFG_DIR+'/'+a+'/'+m)[9])
                                                f_age = currentTime - f_ctime
                                                if f_age > file_min_age:
                                                        fileList[MRTG_CFG_DIR+'/'+a+'/'+m] = f_age
                                                        count = count + 1
                fileList_sorted = sorted(fileList.items(), key=lambda x:x[1], reverse=True)
                n = 0
                for f in fileList_sorted:
                        if n < list_len:
                                os.utime(f[0], None)
                                print(f[0])
                                n = n + 1
                        else:
                                continue
        except:
                print('Exception: ', sys.exc_info())
