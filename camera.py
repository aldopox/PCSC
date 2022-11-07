import cv2

#camera remota (nel caso di smartphone)
def initRemoteCam(IP,port):
    cap = cv2.VideoCapture("rtsp://"+IP+":"+str(port)+"/live.sdp")
    return cap


#camera locale
def initLocalCam(camID):  
    cam = cv2.VideoCapture(camID) #0=front-cam, 1=back-cam
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 460)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    return cam

#leggi immagine da camera
def readImage(cam):
    ret, frame = cam.read()

    return frame