
# coding: utf-8

# In[82]:

from copy import deepcopy


# In[2]:

def normalize(q):
    s = 0
    row_num = len(q)
    col_num = len(q[0])
    for i in range(row_num):
        for j in range(col_num):
            s = s + q[i][j]
    for i in range(row_num):
        for j in range(col_num):
            q[i][j] = q[i][j] / s
    return q


# In[88]:

def move(p, motion, p_move):
    row_num = len(p)
    col_num = len(p[0])
    q = deepcopy(p)
    
    # Initialize q with zeros
    for i in range(row_num):
        for j in range(col_num):
            q[i][j] = 0
    
    for i in range(row_num):
        for j in range(col_num):
            # When the move is successful:
            affected_row = (i + motion[0]) % row_num 
            affected_col = (j + motion[1]) % col_num
            q[affected_row][affected_col] += p_move * p[i][j]
            
            # When the move is not successful:
            q[i][j] += (1 - p_move) * p[i][j];
            
    return normalize(q)


# In[84]:

def measure(p, colors, measurement, sensor_right):
    q = deepcopy(p)
    row_num = len(p)
    col_num = len(p[0])
    for i in range(row_num):
        for j in range(col_num):
            hit = (colors[i][j] == measurement)
            q[i][j] = p[i][j] * (sensor_right * hit + (1 - sensor_right) * (1 - hit))
    return normalize(q)


# In[5]:

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    for i in range(len(measurements)):
        p_after_move = move(p, motions[i], p_move)
        p = measure(p_after_move, colors, measurements[i], sensor_right)
    # >>> Insert your code here <<<
    
    return p


# In[6]:

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


# In[56]:

def are_same(a,b):
    print(a, b)
    if(len(a) != len(b)):
        print("the 1st dimention is not the same")
        return False
    elif(len(a[0]) != len(b[0])):
        print("the 2nd dimention is not the same")
        return False
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                if(math.fabs(a[i][j] - b[i][j]) > 0.01):
                    print("the difference is bigger than 0.01")
                    return False
    return True


# In[111]:

# test 1
colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0]])

assert correct_answer == p 

# test 2
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.5, 0.5],
     [0.0, 0.0, 0.0]])

assert correct_answer == p 

# test 3
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.06666666666, 0.06666666666, 0.06666666666],
     [0.06666666666, 0.26666666666, 0.26666666666],
     [0.06666666666, 0.06666666666, 0.06666666666]])

assert are_same(correct_answer,p) 

# test 4
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.03333333333, 0.03333333333, 0.03333333333],
     [0.13333333333, 0.13333333333, 0.53333333333],
     [0.03333333333, 0.03333333333, 0.03333333333]])

assert are_same(correct_answer,p) 

# test 5
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 0.0]])

assert are_same(correct_answer,p) 

# test 6
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0289855072, 0.0289855072, 0.0289855072],
     [0.0724637681, 0.2898550724, 0.4637681159],
     [0.0289855072, 0.0289855072, 0.0289855072]])

assert are_same(correct_answer,p) 

# test 7
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.33333333, 0.66666666],
     [0.0, 0.0, 0.0]])

assert are_same(correct_answer,p) 

# The final test in the exercise
colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)

correct_answer = [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
[0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
[0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
[0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]

assert are_same(correct_answer,p) 


# In[ ]:




# In[ ]:



