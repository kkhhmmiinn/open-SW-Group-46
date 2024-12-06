import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.my_hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def get_frame(self):
        success, img = self.cap.read()
        if not success:
            return None, None
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img, self.my_hands.process(imgRGB)

    def draw_landmarks(self, img, handLms):
        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
