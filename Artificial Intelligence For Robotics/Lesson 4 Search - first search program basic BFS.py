
# coding: utf-8

# In[6]:

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
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']




# In[25]:

notVisited = 999

def validate(g, grid, node):
    if(-1 < node[1] < len(grid) and -1 < node[2] < len(grid[0]) 
       and grid[node[1]][node[2]] == 0
       and g[node[1]][node[2]] == notVisited):
        return True
    return False    
    
def search(grid, init, goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # The cost matrix
    g = []
    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[0])):
            newRow.append(notVisited)
        g.append(newRow)
    
    waiting_list = [[0, init[0], init[1]]]
    g[init[0]][init[1]] = 0
    
    while(len(waiting_list) > 0):
        currNode = waiting_list[0]
        # print("waiting_list:" + str(waiting_list))
        waiting_list.pop(0)
        
        if(currNode[1] == goal[0] and currNode[2] == goal[1]):
            return currNode
        else:
            for i in range(len(delta)):
                newNode = [-1, currNode[1] + delta[i][0], currNode[2] + delta[i][1]]
                if(validate(g, grid, newNode)):                    
                    g[newNode[1]][newNode[2]] = g[currNode[1]][currNode[2]] + cost
                    newNode[0] = g[newNode[1]][newNode[2]]
                    # print("new node:" + str(newNode))
                    waiting_list.append(newNode)
                    
    return("fail")


# In[24]:

print(search(grid,init,goal,cost))