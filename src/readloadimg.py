################################# Vision por Computador ###############################################
# @author Miguel Angel                                                                                #
# 31 de marzo/20                                                                                      #
########################################## Imports ####################################################
import numpy                                                                                          #
import cv2                                                                                            #                                                                                    #
#######################################################################################################

panda_image = cv2.imread("img/panda.jpg")
panda_gray_image = cv2.cvtColor(panda_image,
                                cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray panda", panda_gray_image)
cv2.imshow("Color panda", panda_gray_image)
cv2.imwrite("img/gray_panda.jpg", panda_gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



