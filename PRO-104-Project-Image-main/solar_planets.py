import cv2
img=cv2.imread("solar-systems.jpg")
cv2.putText(img,  
           "mercury",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "venus",
           (40, 210),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "earth",
           (60, 205),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "mars",
           (80, 205),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "jupiter",
           (100, 180),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "saturn",
           (120, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "uranus",
           (140, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "neptune",
           (160, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )                                                                             
cv2.imshow("output",img)
cv2.waitKey(0)
