import argparse
import pandas as pd
import os

def greeting(name, age, ):
    #print
    print(f"Hello, {name}! You are {age} years old.")

def main(name, age):
    greeting(name, age)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="This is a sample script to test argparse from the terminal.")
    parser.add_argument("-n", "--name", default="Ryan", help="Input your name")
    parser.add_argument("-a", "--age", default=28, type=int, help="Your age in years")
    args = vars(parser.parse_args())
    name = args["name"]
    age = args["age"]
    main(name, age)