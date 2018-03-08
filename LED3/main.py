import urllib.request
import re

import argparse
import requests


#@click.command()
#@click.option("--input", default=None, help="input URI (file or URL)")
def countLightsOn(N, a2d):
    count = 0
    for i in range(N):
        for j in range(N):
            if a2d[i][j] == 1:
                count += 1
                
    return count

# Turn lights that are off (0) to on (1)
def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            a2d[i][j] = 1
            
    return


# Turn lights off that are on (1) to off (0)
def turnOff(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            a2d[i][j] = 0
            
    return

# Switch lights that are on (1) to off (0) and lights that are off (0) to on (1) 
def switch(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if a2d[i][j] == 0:
                a2d[i][j] = 1
            elif a2d[i][j] == 1:
                a2d [i][j] = 0
                
    return


def split(line):
    
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""
    cmd = ""
    
    newLine = line
    newLine = cmd.replace("through", " ")
    newLine = cmd.replace("\n", ",")
    
    
    
    if newLine.startswith("turn on"):
        cmd = "turn on"
        newLine = newLine.replace("turn on", "")
        
    elif newLine.startswith("turn off"):
        cmd = "turn off"
        newLine = newLine.replace("turn off", "")
        
    elif newLine.startswith("switch"):
        cmd = "switch"
        newLine = newLine.replace("switch", "")
        
    elif cmd != "":
        newLine = newLine.replace(",", "")
        val = [int(s) for s in newLine.split() if s.isdigit()]
        
        x1 = val[0]
        x2 = val[2]
        y1 = val[1]
        y2 = val[3]
        
    return cmd, x1, x2, y1, y2
        
   
        
def main() -> object:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    
    uri = filename
    r = urllib.request.Request(filename)
    response = urllib.request.urlopen(r)
    buffer = response.read().decode('utf-8')
    
    a2d = []
    
    for line in buffer.split('\n'):
        
        if line == "":
            break
        
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
    print("Number of occupied lights: ", count)
    
    
    return
        
    

if __name__ == "__main__":
    main()