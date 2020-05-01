# Qumulo tree walk and fix btime/ctime to equal mtime

`fix_timestamps.py`

Walk the specified tree and for each file set ctime and btime to equal mtime.

The majority of this is copied from the treewalk script at 
https://github.com/Qumulo/power-tools/blob/master/api-tree-walk.py

## Requirements
* python 2.7.15 or later.  NOTE: Python 3 is not supported.
* appropriate Qumulo API library `pip install qumulo-api`

## Usage
1. Make sure you have the python requirements: `pip install -r requirements.txt`
2. `python fix_timestamps.py -s qumulo -p ********* -d /home`


