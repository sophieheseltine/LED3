import urllib.request

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
def turnLightsOnOff(x1, x2, y1, y2, a2d, cmd):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if a2d[i][j] == 0 and (cmd == "turn on" or cmd == "switch"):
                a2d[i][j] = 1
                
            elif a2d[i][j] == 1 and (cmd == "turn off" or cmd == "switch"):
                a2d[i][j] = 0
            
    return a2d


def split(line):
    
    newLine = line
    newLine = newLine.replace("through", "")
    newLine = newLine.replace("\n", ",")
    
    if line.startswith(" "):
        newLine = newLine.strip()
    if line.endswith(" "):
        newLine = newLine.strip()
    
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""
    cmd = ""

    if newLine.startswith("turn on"):
        cmd = "turn on"
        newLine = newLine.replace("turn on", "")
        
    if newLine.startswith("turn off"):
        cmd = "turn off"
        newLine = newLine.replace("turn off", "")
        
    if newLine.startswith("switch"):
        cmd = "switch"
        newLine = newLine.replace("switch", "")
        
    if cmd != "":
        newLine = newLine.replace(",", " ")
        
        val = [int(s) for s in newLine.split() if s.isdigit()]
        
        x1 = val[0]
        x2 = val[2]
        y1 = val[1]
        y2 = val[3]
        
    return cmd, x1, x2, y1, y2
        
        
# This function ensures that negative numbers cannot be used for 
# the coordinates and that the coordinates cannot be greater than 
# the size of the grid.
def cleanUp(x1, x2, y1, y2, N):

    if int(x1) < 0:
        x1 = 0
    if int(x2) < 0:
        x2 = 0
    if int(y1) < 0:
        y1 = 0
    if int(y2) < 0:
        y2 = 0

    if int(x1) >= N:
        x1 = N-1
    if int(x2) >= N:
        x2 = N-1
    if int(y1) >= N:
        y1 = N-1
    if int(y2) >= N:
        y2 = N-1

    return x1, x2, y1, y2
    

   
# Parse input        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    
    uri = filename
    r = urllib.request.Request(filename)
    response = urllib.request.urlopen(r)
    buffer = response.read().decode('utf-8')
    
    a2d = []
    
    
    # Make the grid
    for line in buffer.split('\n'):
        
        if line == "":
            break
        
        if line.isdigit():
            N = int(line)
            a2d = [[0]*N for _ in range(N)]
                         
        else:
            command, x1, x2, y1, y2 = split(line)
            
            if command == "turn on" or command == "turn off" or command == "switch":
                
                x1, x2, y1, y2 = cleanUp(x1, x2, y1, y2, N)
                
                if int(x1) <= int(x2) and int(y1) <= int(y2):
                    turnLightsOnOff(int(x1), int(x2), int(y1), int(y2), a2d, command)


    count = countLightsOn(N, a2d)
    print("Number of occupied lights: ", count)
    
    
    return
        
    

if __name__ == "__main__":
    main()