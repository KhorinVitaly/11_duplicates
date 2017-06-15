# Anti-Duplicator

The script finds all file duplicates in specified directory and also in child directories. 
It compare name and size of files. 
 
# Quickstart

You will need python 3.5 interpreter. Then you can launch 
script in terminal or import functions in your code. 

launch on Linux, Python 3.5:

```#!bash

$ python3 duplicates.py <path to directory for check>
#output example
Directory contain duplicates:
./.git/logs/HEAD
./.git/logs/refs/remotes/origin/HEAD
```

Example of using functions in code:

```
import duplicates

files = find_files(your_path)
print(recognize_duplicates(files))

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
