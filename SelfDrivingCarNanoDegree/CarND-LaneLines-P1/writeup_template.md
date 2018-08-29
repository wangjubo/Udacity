# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"
[summary]: ./test_images_output/summary.png

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 steps.
* Convert color image into grey scale
* Edge detection
* Only focus on front of image
* Line detection using Hough transformation
* Average the left and right lines into 2 lines only
* Annotate the detected lane to original image

In order to draw a single line on the left and right lanes, I modified the `draw_lines()` function by creating another function `draw_avged_lines()`, which average all lines into 2 lines, according to their grediants.

Special treatment is done to deal with challenging cases where part of car's front bumper is in view. So the slope of lines are limited to be bigger than 0.2, as can be seen in `avg_all_lines_to_2_lines()` function.

Intermediate results running all these 6 steps:
![Summary image][summary]


### 2. Identify potential shortcomings with your current pipeline

There're at  least 2 shortcoming:
#### a. Similar road color and lane color
**Problem:** One shortcoming would be when the color of road is very similar to the color of lane line. This problem is found in the challenge video.
**Solution:** Potential solution include tuning the color->grey scale transformation to be more sensitive around yellow and white color, the colors of normal road lane lines.

#### b. Sharp turn
**Problem:** Another shortcoming happens at turning - when any feature at road side, when the car is turning, has similar line direction to the lane, it may be included in averaging the line. When a car is turning, the needed image is not exactly in front of the car, but towards a turn direction.
**Solution:** Potential solution include detecting the turning angle, and move the mask towards the turning direction.




### 3. Suggest possible improvements to your pipeline

See solution parts of point 2.
