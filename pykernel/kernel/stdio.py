import os
import sys

# Read Stdout on the System level, but it's like reading from the Operation System level.
# Hardware <- Operating System <- (other OS things ...) <- PyKernel

def readln():
    return sys.stdout.readline()

def writeln(str):
    sys.stdout.write(str + "\n")