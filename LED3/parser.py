'''
@author: sophieheseltine
'''
'''
import argparse
import urllib.request
import requests


def main(input):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    
    #uri = filename
    #request = urllib.request.Request(File)
    #response = urllib.request.urlopen(request)
    #buffer = response.read().decode('utf-8')
    
    uri = filename
    r = urllib.request.Request(filename)
    response = urllib.request.urlopen(r)
    buffer = response.read().decode('utf-8')
    
    a2d = []
    
    for line in buffer.split('\n'):
        if line.isdigit():
            N = int(line)
            a2d = [[0] * N for _ in range(N)]
                         
        else:
            command, x1, x2, y1, y2 = split(line)
            if command == "turn on":
                if int(x1) <= int(x2) and int(y1) <= int(y2):
                    turnOn(int(x1), int(x2), int(y1), int(y2), a2d)
                    
                elif command == "turn off":
                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        turnOff(int(x1), int(x2), int(y1), int(y2), a2d)
                    
                elif command == "switch":
                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        switch(int(x1), int(x2), int(y1), int(y2), a2d)

#print('\n'.join(r.split('\n')))

    count = countLightsOn(N, a2d)
    print(count)
    
    return
'''

#if __name__ == '__main__':
#    main()
    
    