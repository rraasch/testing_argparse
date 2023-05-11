import argparse
import pandas as pd
import os

# Parse command line arguments
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", default="Ryan", help="Name")
parser.add_argument("-a", "--age", default=28, type=int, help="Your age in years")
args = vars(parser.parse_args())

#setup parameters
name = args['name']
age = args['age']

#print
print(f"Hello, {name}! You are {age} years old.")