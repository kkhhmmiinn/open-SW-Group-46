from hand_tracking import HandTracker
from finger_state import FingerState
from gesture_recognition import GestureRecognition
import cv2

if __name__ == "__main__":
    print("Program Start...")
    tracker = HandTracker()
    finger_state = FingerState()
    gesture_recognition = GestureRecognition()

    while True:
        img, results = tracker.get_frame()
        if img is None:
            continue

        if results and results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                open_states = finger_state.update(handLms)
                recognized_gesture = gesture_recognition.recognize(open_states)

               
                if recognized_gesture:
                    h, w, _ = img.shape
                    text_x = int(handLms.landmark[0].x * w)
                    text_y = int(handLms.landmark[0].y * h)
                    cv2.putText(img, recognized_gesture, (text_x - 50, text_y - 50),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

                tracker.draw_landmarks(img, handLms)

        cv2.imshow("HandTracking", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tracker.release()
    print("Program End...")
