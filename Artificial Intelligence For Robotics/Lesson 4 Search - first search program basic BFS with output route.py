
# coding: utf-8

# In[63]:

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

# delta_name = ['^', '<', 'v', '>']
delta_name = ['v', '>', '^', '<']


# In[64]:

notVisited = 999

def Validate(g, grid, node):
    if(-1 < node[1] < len(grid) and -1 < node[2] < len(grid[0]) 
       and grid[node[1]][node[2]] == 0
       and g[node[1]][node[2]] == notVisited):
        return True
    return False


# In[65]:

def CalcRouteFromExpandMatrix(expand, grid, init, goal):
    # Initialize the route matrix with ' '
    route= []
    rowNum = len(expand)
    colNum = len(expand[0])
    for i in range(rowNum):
        newRow = []
        for j in range(colNum):
            newRow.append(' ')
        route.append(newRow)

    # Reversely fill in each grid point on the route with correct direction signroute[goal[0]][goal[1]] = '*'
    currNode = [goal[0], goal[1]]
    route[goal[0]][goal[1]] = '*'
    while True:
        # Potential last node in route, the node with smallest number in 'expand' matrix
        # Assign an initial nodeWithMinimumOrderNumber
        for i in range(len(delta)):
            potentialLastNode = [currNode[0] + delta[i][0], currNode[1] + delta[i][1]]
            if(-1 < potentialLastNode[0] < rowNum 
              and -1 < potentialLastNode[1] < colNum
              and grid[potentialLastNode[0]][potentialLastNode[1]] == 0):
                nodeWithMinimumOrderNumber = [currNode[0] + delta[i][0], currNode[1] + delta[i][1]]
                indexOfNodeWithMinimumOrderNumber = i
                break

        # Find the node with minimum score
        for i in range(len(delta)):
            potentialLastNode = [currNode[0] + delta[i][0], currNode[1] + delta[i][1]]
            if(-1 < potentialLastNode[0] < rowNum 
              and -1 < potentialLastNode[1] < colNum
              and grid[potentialLastNode[0]][potentialLastNode[1]] == 0
              and expand[potentialLastNode[0]][potentialLastNode[1]] < expand[nodeWithMinimumOrderNumber[0]][nodeWithMinimumOrderNumber[1]]):
                # if the nextNode's score is smaller than the current minimum, replace nextNode with the current potentialPoint
                nodeWithMinimumOrderNumber = [potentialLastNode[0], potentialLastNode[1]]
                indexOfNodeWithMinimumOrderNumber = i

        route[nodeWithMinimumOrderNumber[0]][nodeWithMinimumOrderNumber[1]] = delta_name[indexOfNodeWithMinimumOrderNumber]
        
        currNode = [nodeWithMinimumOrderNumber[0], nodeWithMinimumOrderNumber[1]]
        
        if (currNode[0] == 0 and currNode[1] == 0):
            break
    return route


# In[66]:

# a search function that returns 'route' matrix
def search(grid, init, goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # The cost matrix
    g = []
    expand= []
    for i in range(len(grid)):
        newGRow = []
        newExpandRow = []
        for j in range(len(grid[0])):
            newGRow.append(notVisited)
            newExpandRow.append(-1)
        g.append(newGRow)
        expand.append(newExpandRow)
    
    waiting_list = [[0, init[0], init[1]]]
    g[init[0]][init[1]] = 0
    expandIndex = 0
    
    while(len(waiting_list) > 0):
        currNode = waiting_list[0]
        expand[currNode[1]][currNode[2]] = expandIndex
        expandIndex = expandIndex + 1
        waiting_list.pop(0)
        
        for i in range(len(delta)):
            newNode = [-1, currNode[1] + delta[i][0], currNode[2] + delta[i][1]]
            if(Validate(g, grid, newNode)):                    
                g[newNode[1]][newNode[2]] = g[currNode[1]][currNode[2]] + cost
                newNode[0] = g[newNode[1]][newNode[2]]
                waiting_list.append(newNode)
    for line in range(len(expand)):
        print(expand[line])
    route = CalcRouteFromExpandMatrix(expand, grid, init, goal)
    
    return route

# In[67]:

result = search(grid,init,goal,cost)
for line in range(len(result)):
    print(result[line])