
# coding: utf-8

# In[78]:

# -----------------
# USER INSTRUCTIONS
#
# Write a function in the class robot called move()
#
# that takes self and a motion vector (this
# motion vector contains a steering* angle and a
# distance) as input and returns an instance of the class
# robot with the appropriate x, y, and orientation
# for the given motion.
#
# *steering is defined in the video
# which accompanies this problem.
#
# For now, please do NOT add noise to your move function.
#
# Please do not modify anything except where indicated
# below.
#
# There are test cases which you are free to use at the
# bottom. If you uncomment them for testing, make sure you
# re-comment them before you submit.

from math import *
import random
# --------
# 
# the "world" has 4 landmarks.
# the robot's initial coordinates are somewhere in the square
# represented by the landmarks.
#
# NOTE: Landmark coordinates are given in (y, x) form and NOT
# in the traditional (x, y) format!

landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]] # position of 4 landmarks
world_size = 100.0 # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi/4 # You don't need to use this value, but it is good to keep in mind the limitations of a real car.

# ------------------------------------------------
# 
# this is the robot class
#

class robot:

    # --------

    # init: 
    #	creates robot and initializes location/orientation 
    #

    def __init__(self, length = 10.0):
        self.x = random.random() * world_size # initial x position
        self.y = random.random() * world_size # initial y position
        self.orientation = random.random() * 2.0 * pi # initial orientation
        self.length = length # length of robot
        self.bearing_noise  = 0.0 # initialize bearing noise to zero
        self.steering_noise = 0.0 # initialize steering noise to zero
        self.distance_noise = 0.0 # initialize distance noise to zero
    
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))
    # --------
    # set: 
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise (ValueError, 'Orientation must be in [0..2pi]')
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)


    # --------
    # set_noise: 
    #	sets the noise parameters
    #

    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.bearing_noise  = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)
    
    ############# ONLY ADD/MODIFY CODE BELOW HERE ###################

    # --------
    # move:
    #   move along a section of a circular path according to motion
    #

    def move(self, motion, tolerance = 0.0001): # Do not change the name of this function

        # ADD CODE HERE
        steering_alpha = motion[0] + 1e-20
        distance = motion[1]
        
        # Valiate input data
        if(abs(steering_alpha) > max_steering_angle):
            raise(ValueError, 'Exceeded max steering angle')
        
        if(distance < 0):
            raise(ValueError, 'Distance cannot below zero')
        
        # Apply noise
        steering_alpha_with_noise = random.gauss(steering_alpha, self.steering_noise)
        distance_with_noise = random.gauss(distance, self.distance_noise)

        turn_beta = distance_with_noise / self.length * tan(steering_alpha_with_noise)
        
        result = robot()
        result.length = self.length
        result.bearing_noise  = self.bearing_noise
        result.steering_noise = self.steering_noise
        result.distance_noise = self.distance_noise
        
        self_orientation_theta = self.orientation
        if(abs(turn_beta) < tolerance):
            result.x = self.x + distance_with_noise * cos(self_orientation_theta)
            result.y = self.y + distance_with_noise * sin(self_orientation_theta)
            result.orientation = (self_orientation_theta + turn_beta) % (2.0 * pi)
        else:        
            R = distance_with_noise / turn_beta
            cx = self.x - sin(self_orientation_theta) * R
            cy = self.y + cos(self_orientation_theta) * R
            result.orientation = (self_orientation_theta + turn_beta) % (2.0 * pi)
            result.x = cx + sin(result.orientation) * R
            result.y = cy - cos(result.orientation) * R
                  
        
        return result # make sure your move function returns an instance
                      # of the robot class with the correct coordinates.

    ############## ONLY ADD/MODIFY CODE ABOVE HERE ####################
    
    


# In[79]:



## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## move function with randomized motion data.

## --------
## TEST CASE:
## 
## 1) The following code should print:
##       Robot:     [x=0.0 y=0.0 orient=0.0]
##       Robot:     [x=10.0 y=0.0 orient=0.0]
##       Robot:     [x=19.861 y=1.4333 orient=0.2886]
##       Robot:     [x=39.034 y=7.1270 orient=0.2886]
##
##
length = 20.
bearing_noise  = 0.0
steering_noise = 0.0
distance_noise = 0.0
##
myrobot = robot(length)
myrobot.set(0.0, 0.0, 0.0)
myrobot.set_noise(bearing_noise, steering_noise, distance_noise)
##
motions = [[0.0, 10.0], [pi / 6.0, 10], [0.0, 20.0]]
##motions = [[0.2, 10.] for row in range(10)]
##
T = len(motions)
##
print('Robot:    ', myrobot)
for t in range(T):
    myrobot = myrobot.move(motions[t])
    print('Robot:    ', myrobot)



## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## move function with randomized motion data.


# In[29]:




# In[ ]:



