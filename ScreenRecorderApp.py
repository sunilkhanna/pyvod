import pyautogui
import cv2
import numpy as np
from cv2 import VideoCapture, VideoWriter


# -----------StartWeb Camera------------//

def selectCamera(inputcamera):
    print('camera selected', inputcamera)
    cap = cv2.VideoCapture(inputcamera)

    if not cap.isOpened():
        print('can not open camera')
        exit()
    return cap

''' Define webcam background support'''

def backgroundProcessor():
    return NULL

 



def startCapturing(videoObj: VideoCapture):
    out = initVideoWriter()
    width = 150
    height = 180
    dim = (width, height)
    # fgbg = cv2.createBackgroundSubtractorMOG2()
    while True:
        videoObj.set(3, 100)
        videoObj.set(4, 100)
        ret, frame = videoObj.read()
        if not ret:
            print('cant recv frame')
            break
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame',gray)

        # cv2.resizeWindow('frame',350,350)
        # cv2.createHanningWindow((400,400),cv2.CV_32F)
        #    fgmask = fgbg.apply(frame)
        
        
        ''' ----------------- '''
        key = cv2.waitKey(1) & 0xff
        if key == ord('p'):
            while True:
                key2=cv2.waitKey(1) & 0xff
                cv2.imshow('frame', frame)
                cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
                
                if key2 == ord('p'):
                    break
        
        cv2.imshow('frame', frame)        
        recordScreen(out)        

        
        '''________________ '''
        if cv2.waitKey(1) == ord('q'):
            break
    releaseScreen(out)
    releaseCam(videoObj)

    destroyWin()


def releaseCam(videoObj: VideoCapture):
    videoObj.release()


def releaseScreen(videoScrn: VideoWriter):
    videoScrn.release()


def destroyWin():
    cv2.destroyAllWindows()


# --------Start screen recording----------//

def initVideoWriter():
    print('Video writer initializing....')
    resolution = (1920, 1080)
    codec = cv2.VideoWriter.fourcc(*'XVID')
    filename = "Recording.avi"
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)
    return out


def recordScreen(out: VideoWriter):
    # while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)
    # Convert it from BGR(Blue, Green, Red) toq`q`
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('Live', frame)
    out.write(frame)


startCapturing(selectCamera(0))
