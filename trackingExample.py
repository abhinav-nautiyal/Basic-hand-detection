import cv2
import time
import handTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Change to 1 if using an external camera
detector = htm.handDetector()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from the camera. Check camera index.")
        break

    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(f"Landmark 4 (thumb tip) position: {lmList[4]}")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on pressing 'q'
        break

cap.release()
cv2.destroyAllWindows()
