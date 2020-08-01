import cv2
from PIL import Image
import matplotlib
from datetime import datetime

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
now = datetime.now()
# print(now)

fno=0
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key == 32: #space to capture image
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(rgb)
        im.save("webcam"+str(now)+str(fno)+".jpeg")
        fno+=1

vc.release()
cv2.destroyWindow("preview")