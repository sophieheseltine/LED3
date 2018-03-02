'''
@author: sophieheseltine
'''

import argparse


def parseFile(input):
    
    if input.startswith('http'):
        #use requests
        pass
    else:
        #read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        #no code written yet
        return N, instructions
    return


parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input