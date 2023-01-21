#Ahsas Srivastava
import cv2
import webbrowser
# initalize the webcam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect the image and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # checks if there is a QRCode in the image
    if data:
        a=data
        break
    # result gets displayed
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()