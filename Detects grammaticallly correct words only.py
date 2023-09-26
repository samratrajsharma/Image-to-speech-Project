import cv2
import pytesseract
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
camera = cv2.VideoCapture(0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    _, frame = camera.read()

    detected_text = pytesseract.image_to_string(frame)

    if detected_text:
        matches = tool.check(detected_text)
        if not matches:
            print("Detected text:", detected_text)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()