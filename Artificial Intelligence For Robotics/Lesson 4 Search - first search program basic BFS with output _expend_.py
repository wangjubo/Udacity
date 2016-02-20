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

delta_name = ['^', '<', 'v', '>']

notVisited = 999

def validate(g, grid, node):
    if(-1 < node[1] < len(grid) and -1 < node[2] < len(grid[0]) 
       and grid[node[1]][node[2]] == 0
       and g[node[1]][node[2]] == notVisited):
        return True
    return False    

# a search function that returns 'expend' matrix
def search(grid, init, goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # The cost matrix
    g = []
    expend= []
    for i in range(len(grid)):
        newGRow = []
        newExpendRow = []
        for j in range(len(grid[0])):
            newGRow.append(notVisited)
            newExpendRow.append(-1)
        g.append(newGRow)
        expend.append(newExpendRow)
    
    waiting_list = [[0, init[0], init[1]]]
    g[init[0]][init[1]] = 0
    expendIndex = 0
    
    while(len(waiting_list) > 0):
        currNode = waiting_list[0]
        expend[currNode[1]][currNode[2]] = expendIndex
        expendIndex = expendIndex + 1
        waiting_list.pop(0)
        
        for i in range(len(delta)):
            newNode = [-1, currNode[1] + delta[i][0], currNode[2] + delta[i][1]]
            if(validate(g, grid, newNode)):                    
                g[newNode[1]][newNode[2]] = g[currNode[1]][currNode[2]] + cost
                newNode[0] = g[newNode[1]][newNode[2]]
                waiting_list.append(newNode)
                    
    return expend

print(search(grid,init,goal,cost))

