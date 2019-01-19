import cv2
from imutils import paths

def draw_detections(img, rects, thickness = 1,color = (0,255,0)):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        cv2.rectangle(img, (x, y), (x+w, y+h),color, thickness)

vc = cv2.VideoCapture(0)

if vc.isOpened():
    open, img = vc.read()
else:
    open = False
hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector())
face_recog = cv2.face_BasicFaceRecognizer()#
face_recog.train()

while open:

    #Get the video capture frame.
    open, img = vc.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bodies,w=hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)

    draw_detections(img,bodies)

    # Display the resulting frame
    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
vc.release()
cv2.destroyAllWindows()