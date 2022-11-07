from camera import * # *= importa tutto quello che ho scritto su camera
from recognizer import * # *= importa tutto quello che ho detto su recognizer
import cv2
import calendar
import time
import requests

def get_cam_id():
    try:
        with open('.camid') as f:
            lines = f.readlines()
        cam_id = lines[0]
    except FileNotFoundError:
        print("Camera configuration file not found.")
        cam_id = input("Insert your camera id here: ")
        f = open(".camid", "w")
        f.write(cam_id)
        f.close()
        print(f"Camera configuration file created for id {cam_id}")
    return cam_id

# TODO: found_objects are a list of items -> list representation is needed
def publish_data(cam_id, found_objects):
    ts = calendar.timegm(time.gmtime())
    url = 'http://127.0.0.1:5000/datastream'
    data = {
        'id': cam_id,
        'timestamp': str(ts) + ', ',
        'found_objects': ', '.join(found_objects),
    }
    r = requests.post(url, data=data)
    print(r.request.body)

IP = "192.168.1.6" #dettagli camera remota (caso smartphone)
port = 8554

cam_id = get_cam_id()
cam = initLocalCam(0)

recognizer = Recognizer()

img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("Ops, qualcosa è andato storto!")
        break
    frame, preds = recognizer.run(frame)
    found_objects = [dict["name"] for dict in preds]
    print(found_objects)
    publish_data(cam_id, found_objects)

    cv2.imshow("", frame)

    k = cv2.waitKey(1)

    if k%256==27:
        print("Chiudo fotocamera")
        break


cam.release()
cv2.destroyAllWindows()
