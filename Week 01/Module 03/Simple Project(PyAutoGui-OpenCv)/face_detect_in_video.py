import cv2

face_cap = cv2.CascadeClassifier("c:/Users/lenovo/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

while True:
    _,frame = video_cap.read()
    color = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        color,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("My Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()