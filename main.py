import cv2
import numpy as np
import pyautogui
from hand_detector import HandDetector

pyautogui.FAILSAFE = False

wCam = 640
hCam = 480

frameR = 100
smoothening = 7

plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

detector = HandDetector()

screenW, screenH = pyautogui.size()

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img)

    if len(lmList) != 0:

        x1, y1 = lmList[8][1], lmList[8][2]

        cv2.rectangle(
            img,
            (frameR, frameR),
            (wCam-frameR, hCam-frameR),
            (255,0,255),
            2
        )

        x3 = np.interp(x1, (frameR, wCam-frameR), (0, screenW))
        y3 = np.interp(y1, (frameR, hCam-frameR), (0, screenH))

        clocX = plocX + (x3-plocX)/smoothening
        clocY = plocY + (y3-plocY)/smoothening

        pyautogui.moveTo(clocX, clocY)

        plocX, plocY = clocX, clocY

        cv2.circle(img,(x1,y1),12,(255,0,255),cv2.FILLED)

        # Left Click

        x2, y2 = lmList[4][1], lmList[4][2]

        length = np.hypot(x2-x1, y2-y1)

        if length < 35:

            cv2.circle(img,((x1+x2)//2,(y1+y2)//2),15,(0,255,0),cv2.FILLED)

            pyautogui.click()

            cv2.waitKey(200)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()