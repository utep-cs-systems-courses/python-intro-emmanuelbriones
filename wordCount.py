import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCountTest.py <input text file> <output file> <solution key file>")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

dictionaryOfWords = {}
