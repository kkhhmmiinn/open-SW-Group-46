class GestureRecognition:
    def __init__(self):
        self.gestures = [
            [True, True, True, True, True, "Paper"],
            [True, True, False, False, False, "Scissors"],
            [False, True, True, False, False, "Scissors"],
            [True, False, False, False, True, "X"],
            [False, True, True, True, False, "X"],
            [True, False, False, False, False, "Rock"]
        ]

    def recognize(self, open_states):
        for gesture in self.gestures:
            if gesture[:5] == open_states:
                return gesture[5]
        return None
