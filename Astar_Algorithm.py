#Below is the implementation of A_Star algorithm
#Simulation of quickly dispersing from class
#a,b and c represent robots placed at different seats
#To disperse quickly, it is assumed that they have to take the shortest path
#Please only change the __main__ function and h function(Heuristics)


from pyamaze import maze,agent,COLOR,textLabel                  #Download library pyamaze first
from queue import PriorityQueue                                 #Use Priority queue
from math import sqrt                                           #To access Sqare root for Euclidean Distance

def h(p1, p2):                                                  #Heuristic
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + abs(y1 - y2))                        #Manhattan Distance (Comment out Euclidean Distance line for this)
#    return sqrt((x1-x2)**2+(y1-y2)**2)                         #Euclidean Distance (Comment out Manhattan distance line for this)
    
def A_Star(m,start=None):                                       #A Star search algorithm
    if start is None:                                           #When start point is not mentioned, Start from (10,10)
        start=(10,10)

    Track_P = {}
    frontier = PriorityQueue()
    frontier.put((h(start, m._goal), h(start, m._goal), start))
    
    g = {row: float("inf") for row in m.grid}                   #Function of Cost so far 
    g[start] = 0
    f = {row: float("inf") for row in m.grid}                   #Function from cost so far and Heuristics 
    f[start] = h(start, m._goal)
    Path_Finding=[start]
    while not frontier.empty():
        pos = frontier.get()[2]
        Path_Finding.append(pos)
        if pos == m._goal:
            break        
        for d in 'ESNW':                                        #ESNW are East, South, North and West. Directions defined in Pyamaze
            if m.maze_map[pos][d]==True:
                if d=='E':
                    current=(pos[0],pos[1]+1)
                elif d=='W':
                    current=(pos[0],pos[1]-1)
                elif d=='N':
                    current=(pos[0]-1,pos[1])
                elif d=='S':
                    current=(pos[0]+1,pos[1])

                g_t = g[pos] + 1                                #Temporary cost so far
                f_t = g_t + h(current, m._goal)                    #Temporary f

                if f_t < f[current]:                               #If temporary f is less than the f current, then update temporary f as f
                    Track_P[current] = pos
                    g[current] = g_t
                    f[current] = g_t + h(current, m._goal)
                    frontier.put((f[current], h(current, m._goal), current))


    Path={}                                                     #Initialize Path taken


    fin=m._goal
    while fin!=start:
        Path[Track_P[fin]]=fin
        fin=Track_P[fin]
    return Path_Finding,Track_P,Path


if __name__=='__main__':                                            #Main function
    m=maze(10,10)                                                   #Initialize "maze", taken from pyamaze library
    m.CreateMaze(loadMaze='Class_Setup1.csv',theme='light')         #Class_Setup1 replicates our class
    
    Path_Finding,Track_P,Path=A_Star(m)                             #A star with (10,10) as start point
    Path_Finding2,Track_P2,Path2=A_Star(m,(10,2))                   #A star with (10,2) as start point
    Path_Finding3,Track_P3,Path3=A_Star(m,(8,8))                    #A star with (8,8) as start point
    
    a = agent(m,footprints=True,color=COLOR.red,filled=True,goal=(1,1))             #For Pathfinding of agent "a"
    aT= agent(m,footprints=True,shape='arrow',color=COLOR.black,goal=(1,1))         #For shortest path of agent "a" 
                                                                                    #Also remove/add shape = 'arrow' according to your preference
    b = agent(m,10,2,footprints=True,color=COLOR.yellow,filled=True,goal=(1,1))     #For Pathfinding of agent "b"
    bT= agent(m,10,2,footprints=True,color=COLOR.red,goal=(1,1))                    #For shortest path of agent "b"
    c = agent(m,8,8,footprints=True,color=COLOR.blue,filled=True,goal=(1,1))        #For Pathfinding of agent "c"
    cT= agent(m,8,8,footprints=True,color=COLOR.blue,goal=(1,1))                    #For shortest path of agent "c"
 
    #m.tracePath({a:Path_Finding},delay=200)                         #To run Path finding Algo for a, Comment out other path finding and vice versa
    m.tracePath({aT:Path},delay=100)                                #Shortest path for a
    #m.tracePath({b:Path_Finding2},delay=200)
    m.tracePath({bT:Path2},delay=100)                               #Shortest path for b
    #m.tracePath({c:Path_Finding3},delay=200)
    m.tracePath({cT:Path3},delay=100)                               #Shortest path for c
    
    #l=textLabel(m,'Blocks searched for a',len(Path_Finding))        #To see the number of blocks searched for a
    #l=textLabel(m,'Blocks searched for b',len(Path_Finding2))      #To see the number of blocks searched for b
    #l=textLabel(m,'Blocks searched for c',len(Path_Finding3))      #To see the number of blocks searched for c
    l=textLabel(m,'Shortest Path length for a',len(Path)+1)         #To see the shortest path transversed for a
    l=textLabel(m,'Shortest Path length for b',len(Path2)+1)        #To see the shortest path transversed for b
    l=textLabel(m,'Shortest Path length for c',len(Path3)+1)        #To see the shortest path transversed for c
    
    m.run()




#Cite: https://github.com/MAN1986/pyamaze, used as a reference