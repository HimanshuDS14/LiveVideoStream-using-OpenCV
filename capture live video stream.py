import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)



    cv2.imshow("output" , frame)

    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()