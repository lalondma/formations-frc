# import the necessary packages
import time
import cv2
import dlib
 

capture = cv2.VideoCapture(0)

detector = dlib.simple_object_detector("detector.svm")

# capture frames from the camera

tracked_det = [] # left,top,right,bottom
tolerance = 20
tracking = False
i=0
while True:

     ret, image = capture.read()
     image=cv2.resize(image,(320,240))
     ovl = image.copy()
  #   cv2.imshow("IMGxx",image)
  #   cv2.waitKey(1)

     if tracking:
        roi_left = tracked_det[0] - tolerance
        if roi_left<0:
           roi_left = 0
        roi_top = tracked_det[1] - tolerance
        if roi_top<0:
           roi_top = 0
        roi_right = tracked_det[2] + tolerance
        if roi_right>=image.shape[1]:
           roi_right = image.shape[1]-1
        roi_bottom = tracked_det[3] + tolerance
        if roi_bottom>=image.shape[0]:
           roi_bottom = image.shape[0]-1        

        image = image[roi_top:roi_bottom, roi_left:roi_right]
     
     
     #tracking=False
     dets = detector(image)
     if len(dets) != 0:
         #print("{} {}".format(dets[0].top(),dets[0].bottom())) 
         if len(dets)==1:
            boite = dets[0]
         else:
            best_boite = None
            dist_to_center = 1000
            for candidat in dets:
               if abs(candidat.left()-IMAGE_CENTER) < dist_to_center:
                   dist_to_center = abs(candidat.left()-IMAGE_CENTER)
                   best_boite = candidat
            boite = best_boite

         left=boite.left()
         top = boite.top()
         right=boite.right()
         bottom=boite.bottom()

         if tracking:
            left += roi_left
            top += roi_top
            right += roi_left
            bottom += roi_top
         cv2.rectangle(ovl,(left,top),(right,bottom),(255,255,0)) 
         tracked_det = [left, top,right,bottom]
         tracking = True

            
     else:
        # print("Rien trouve")
         tracking = False
         time.sleep(.05)
         traked_det = []
 
     # clear the stream in preparation for the next frame
     
     ovl2=cv2.resize(ovl,(640,480))
     cv2.imshow("IMG",ovl2)
     cv2.waitKey(1)

     i+=1


                                                                                

