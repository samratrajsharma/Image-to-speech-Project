import cv2
import pytesseract
import re

def find_repeated_words(text):
    words = text.split()
    word_count = {}
    repeated_words = []

    for word in words:
        clean_word = re.sub(r'[^\w\s]', '', word).lower()
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1

    for word, count in word_count.items():
        if count > 1:
            repeated_words.append(word)

    return repeated_words

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

camera = cv2.VideoCapture(0)
previous_text = None

while True:
    _, frame = camera.read()

    detected_text = pytesseract.image_to_string(frame)

    if detected_text and detected_text != previous_text:
        if len(detected_text.split()) > 1:  # Check if text contains more than one word (likely grammatically correct)
            print("Detected text:", detected_text)

            repeated_words = find_repeated_words(detected_text)
            if repeated_words:
                print("Repeated words:", repeated_words)

        previous_text = detected_text

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()