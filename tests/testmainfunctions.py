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

    
N = 5
a2d = [[0]*N for _ in range(N)]

#turnOn(-1, 1, 2, 2, a2d)
#turnOn(-2, 2, 1, 1, a2d)
#turnOff(, , , , a2d)
#switch(0, 0, 2, 2, a2d)
#switch(0, 0, 1, 1, a2d)

#turnOn(-2, 0, 0, 0, a2d)


for a in a2d:
    print(a)

count = countLightsOn(N, a2d)
print("Number of lights on:", count)