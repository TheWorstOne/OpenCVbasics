################################# Vision por Computador ###############################################
# @author Miguel Angel                                                                                #
# 31 de marzo/20                                                                                      #
########################################## Imports ####################################################
import numpy                                                                                          #
import cv2                                                                                            #
from matplotlib import pyplot as plt                                                                  #                                                                                    #
#######################################################################################################

image = cv2.imread("img/panda.jpg")

# Plotting the histogram
histogram_image = cv2.calcHist([image], [0], None, 
                               [256], [0,256])

# flaten the histogram
plt.hist(histogram_image.ravel(),256, [0,256])
plt.show()

# View color channels
color = ['b','g','r']

# Separate the color and plot the histogram
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, 
                        [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()
