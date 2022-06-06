from sys import stdin
import numpy as np
import cv2
import matplotlib.pyplot as plt

pixels_r = []
pixels_g = []
pixels_b = []

height = 0
width = 0


file = open('/home/nsl48/DeepLearning_Guide/imagechallenge/problem2-day-night/input11.txt')

for line in file:
  line = line.split(" ")
  width = len(line)
  height += 1
  for i in line:
        r,g,b = map(int, i.split(','))
        #print(r,g,b)
        pixels_r.append(r)
        pixels_g.append(g)
        pixels_b.append(b)
        
        
#print(height,width)
image_r = np.array(pixels_r, dtype = np.uint8)
image_r = image_r.reshape(height, width)

image_g = np.array(pixels_g, dtype = np.uint8)
image_g = image_g.reshape(height, width)

image_b = np.array(pixels_b, dtype = np.uint8)
image_b = image_b.reshape(height, width)




rgb_image = np.dstack((image_r, image_g, image_b))
gray = 0.2989 * image_r + 0.5870 * image_g + 0.1140 * image_b



histogram, bin_edges = np.histogram(gray, bins = 256, range = (0, 255))
indice = np.where(histogram == np.amax(histogram))
peak = int(indice[0])
print(peak)


if(peak >37):
    print("day")
else:
    print("night")

