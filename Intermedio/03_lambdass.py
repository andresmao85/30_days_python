# Write a lambda function which can solve a slope or y-intercept of linear functions.

'''Slope is (m = y2-y1/x2-x1). 
x1, y1 = 2, 2
x2, y2 = 6,10
slope_points = (y2 - y1) / (x2 -x1)
'''

slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print(slope(4,6,9,12))