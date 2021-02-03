import cv2
import winsound # for sound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read() # initial
    ret, frame2 = cam.read() # final
    diff = cv2.absdiff(frame1,frame2) # get difference between initial and final
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5, 5), 0)
    _,  thresh = cv2.threshold(blur,20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None, iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2 )
    for c in contours:
        if cv2.contourArea(c) < 5000: # for greater motion area
            continue

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y) ,(x + w, y+h), (0, 255, 0), 2)
        # set the beeb sound
        #winsound.Beep(500, 200) #500 how loud and 200 how long the beep sound
        winsound.PlaySound('sound.wav',winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'): # quit camer
        break
    cv2.imshow('joshan',frame1)