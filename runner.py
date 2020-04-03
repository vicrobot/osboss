"""
at home dir, .bashrc is modified at line 94, alias osb='cd ~/Desktop/projects/osboss && python runner.py'
"""

import os
import sys

file_n =  sys.argv[1:][0]
if file_n == '--help':
    print("OSBOSS DOCS: A high level language as a wrapper to python. Version 0.1.\nSupports initializing variables and addition or subtraction operation on them. Plus theres a 'show' keyword similar to print in python 2"); exit(0)
from compiler_osb.syntax_compiler import osbtopy

with open(file_n, 'r') as script:
    lines = [i for i in script.readlines() if i]

python_code = osbtopy(lines)
exec(python_code)

