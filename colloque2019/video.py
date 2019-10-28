import cv2
 
capture = cv2.VideoCapture(0)
i = 0
while(True):
     
    ret, frame = capture.read()
     
    cv2.imshow('video', frame)
     
    c = cv2.waitKey(1)
    if c == 27:
        break
    if c==32:
        cv2.imwrite("image{}.jpg".format(i),frame)
        print('saved')
        i += 1
    
 
capture.release()
cv2.destroyAllWindows()

