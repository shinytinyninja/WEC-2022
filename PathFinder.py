import collections
# start = (x,y)
# end = (x,y)
# pitstop = [(x,y),(x,y),(x,y)]
# matrix = [][]

def PathFinder(start, end, pitStops, matrix):
    path = bfs(matrix, )
    
    return path



def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))