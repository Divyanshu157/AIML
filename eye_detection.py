import numpy as np
import matplotlib as plt
import cv2

fd =cv2.CascadeClassifier(cv2.data.haarcascade+"haarcascade_frontalface_default.xml")
ed=cv2.CascadeClassifier(cv2.data.haarcascade+"haarcascade_eye_tree_eyeglasses.xml")

captured=True
counter=0

#start video captrue
vid = cv2.VideoCapture(0)

while True:
    
    flag,img=  vid.read()
    if flag:
        
        faces = fd.detectMultiscale(img,1.1,5)     
        for x,y,w,h in faces:
            
            face = img[y:y+h,x:x+w]  # pehle x aayega ya y  sir se puchna hai 
            
            eye = ed.detectMultiscale(img,1.1,200)
            
        
            
            
            
        key = cv2.waitKey(0)
        if key==ord("q"):
            
            break
       
       
            
            
    else :
        break
    
    cv2.destroyAllWindows()
    vid.release()
    
            
            
            
            
            
        
    
