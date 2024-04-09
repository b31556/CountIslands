def findNeig(g,x,y,l):
    try:
        if g[x+1][y] == 1 and not (x-1,y) in l:
            l.append((x+1,y))
            l=findNeig(g,x+1,y,l)
    except:
        pass
    try:
        if g[x-1][y] == 1 and not (x+1,y) in l:
            l.append((x-1,y))
            l=findNeig(g,x-1,y,l)
    except:
        pass
    try:
        if g[x][y+1] == 1 and not (x,y+1) in l:
            l.append((x,y+1))
            l=findNeig(g,x,y+1,l)
    except:
        pass
    try:
        if g[x][y-1] == 1 and not (x,y-1) in l:
            l.append((x,y-1))
            l=findNeig(g,x,y-1,l)
    except:
        pass
    return l


def count(grid):
    lisOE=[]
    num=0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not (x,y) in lisOE:
                if grid[x][y] == 1:
                    lisOE.append((x,y))
                    num+=1
                    lisOE=findNeig(grid,x,y,lisOE)
    return num
    
