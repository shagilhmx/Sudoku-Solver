import cv2
import pytesseract

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(rgb, "")
    print(text)

    """for (x, y, w, h) in texts:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)"""

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
