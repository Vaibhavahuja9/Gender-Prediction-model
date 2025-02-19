#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
img=cv2.imread("D:/project-gender-detect/data/sachin.jpg")
MODEL_MEAN_VALUES=(78.4263377603,87.7689143744,114.895847746)
gender_list=['female','male']

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceDetect=cv2.CascadeClassifier("D:/project-gender-detect/data/haarcascade_frontalface_default.xml")
faces=faceDetect.detectMultiScale(gray)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)#(object,startx,y,endx,y,bgr,thickness)
    
    #get face
    face_img= img[y:y+h,h:h+w].copy()
    blob=cv2.dnn.blobFromImage(face_img,1,(227,227),
    MODEL_MEAN_VALUES,swapRB=False)
    
    gender_net=cv2.dnn.readNetFromCaffe(
        "D:/project-gender-detect/data/deploy_gender.prototxt",
    "D:/project-gender-detect/data/gender_net.caffemodel")
        
    
    #predict gender
    gender_net.setInput(blob)
    gender_preds=gender_net.forward()
    print(gender_preds)
    gender=gender_list[gender_preds[0].argmax()]
    
    cv2.putText(img,gender,(x,y-3),1,1,(255,255,255))
    
cv2.imshow("Faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




