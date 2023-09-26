import cv2
import pytesseract
from gtts import gTTS
import os

camera = cv2.VideoCapture(0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    _, frame = camera.read()

    detected_text = pytesseract.image_to_string(frame)

    if detected_text:
        print("Detected text:", detected_text)

        tts = gTTS(detected_text, lang='en')

        tts.save("output.mp3")

        os.system("start output.mp3")
        
        folder_path = 'C:\data'
        file_name = 'output.mp3'

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        audio_path = os.path.join(folder_path, file_name)
        tts.save(audio_path)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
