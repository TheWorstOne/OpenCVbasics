################################# Vision por Computador ###############################################
# @author Miguel Angel                                                                                #
# 31 de marzo/20                                                                                      #
########################################## Imports ####################################################
import numpy as np                                                                                    #
import cv2                                                                                            #                                                                                    #
#######################################################################################################

ageofempires_video = cv2.VideoCapture("media/sundiata.mp4")

fcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("media/new_sundiata.avi", fcc, 
                      28, (640,360))

while True:
    ret, frame = ageofempires_video.read()
    frame2 = cv2.flip(frame, 1)
    cv2.imshow("frame2", frame2)
    cv2.imshow("frame", frame)
    out.write(frame2)
    key = cv2.waitKey(20)
    if key == 27:
        break

out.release()
ageofempires_video.release()
cv2.destroyAllWindows()