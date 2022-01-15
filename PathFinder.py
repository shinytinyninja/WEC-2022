import collections
# start = (x,y)
# end = (x,y)
# pitstop = [(x,y),(x,y),(x,y)]
# matrix = [][]

def PathFinder(pitStops, matrix):
    
    attractDict = {}
    wall = []
    #find Location of Attractions
    for row in range(len(matrix)):
        for colom in range(len(matrix[0])):
            if (matrix[row][colom].getObjectName() != "path"):
                attractDict[matrix[row][colom].getObjectName()] = (row, colom)    
                wall.append((row,colom))      
    
    finalPath = []
    
    matrixHeight = len(matrix)
    matrixWidth = len(matrix[0])
    
    for step in range (0, len(pitStops)-1):
        start = attractDict[pitStops[step]]
        
        queue = collections.deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if matrix[x][y].getObjectName() == pitStops[step+1]:
                print("Found a Path")
                finalPath.append(path)
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < matrixWidth and 0 <= y2 < matrixHeight and matrix[x2][y2] != wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
    
    return finalPath