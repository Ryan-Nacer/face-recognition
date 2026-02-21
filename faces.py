from gettext import find
import cv2
import numpy as np
import face_recognition
import os


def findEncodings(imgages):
    encodeList = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoded = face_recognition.face_encodings(image)[0] 
        encodeList.append(encoded)
    return(encodeList)



path = "pictures"
images = []
classNames = []
myList = os.listdir(path)
#print(myList)

for cls in myList:
    image= cv2.imread(f"{path}/{cls}")
    images.append(image)
    classNames.append(os.path.splitext(cls)[0])

print(classNames)

encodeKnownList = findEncodings(images)
print ("done encoding")


cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    if not success or img is None:
        print("Failed to capture image from camera")
        continue  # skip this frame

    imgN = cv2.resize(img,(0,0),None, 0.5,0.5)
    imgN = cv2.cvtColor(imgN, cv2.COLOR_BGR2RGB)

    facesNow = face_recognition.face_locations(imgN)
    encodesNow = face_recognition.face_encodings(imgN)

    for encode,face in zip(encodesNow,facesNow):
        result = face_recognition.compare_faces(encodeKnownList,encode)
        distance = face_recognition.face_distance(encodeKnownList,encode)
        #print (distance)
        matchIndex = np.argmin(distance)

        if result[matchIndex]:
            name = classNames[matchIndex]
            x1,y1,x2,y2=face
            x1,y1,x2,y2=x1*2,y1*2,x2*2,y2*2
            cv2.rectangle(img,(y1,x1),(y2,x2),(0,255,0),2)
            cv2.putText(img, name.upper(), (y2+6,x1-6),cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)

    cv2.imshow("webcam",img)
    cv2.waitKey(1)
