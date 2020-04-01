################################# Vision por Computador ###############################################
# @author Miguel Angel                                                                                #
# 31 de marzo/20                                                                                      #
########################################## Imports ####################################################
import numpy as np                                                                                    #
import cv2                                                                                            #                                                                                    #
#######################################################################################################

ageofempires_video = cv2.VideoCapture("media/sundiata.mp4")

while True:
    ret, frame = ageofempires_video.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(25)
    if key == 27:
        break

ageofempires_video.release()
cv2.destroyAllWindows()