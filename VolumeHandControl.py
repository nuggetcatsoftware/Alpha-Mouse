import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import pycaw    
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#variables
wCam,hCam=640,488 #640,488
pTime=0
vol=0
detector=htm.handDetector(detectionCon=0.7,maxHands=2)
volBar=400


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange=volume.GetVolumeRange() #-65.25,0
#volume.SetMasterVolumeLevel(-20.0, None)
minVol=volRange[0]
maxVol=volRange[1]

########
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img,draw=False)
    if len(lmList)>0:
        #for only these 2 values thumb and finger tip
        x1, y1= lmList[4][1], lmList[4][2]
        x2, y2= lmList[8][1], lmList[8][2]
        ####################
        cx,cy=(x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1,y1),7,(255,0,0),cv2.FILLED)
        cv2.circle(img, (x2,y2),7,(255,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.circle(img,(cx,cy),7,(255,0,0),cv2.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        print(length)
        #hand range max 300 to min 50
        #vol range -65 to 0
        

        vol =np.interp(length, [50,180],[minVol,maxVol]) #designed for short fingers lmao
        
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)
        vol=np.interp(length,[50,300],[minVol,maxVol])
        volBar=np.interp(length,[50,300],[400,150])
        if length<50:
            cv2.circle(img,(cx,cy),7,(0,255,0),cv2.FILLED)
    cv2.rectangle(img,(50,150),(85,400),(58, 88, 222),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(58, 88, 222),cv2.FILLED)

    

#frame rate
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(50,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,
    2,(0,255,0),3)


#show img
    cv2.imshow("img",img)
    cv2.waitKey(1)