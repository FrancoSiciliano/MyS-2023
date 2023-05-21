import tkinter as tk
from welcome_page import WelcomePage


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frame_stack = []

        self.ws = WelcomePage(self)

        self.switch_frame(self.ws)

    def switch_frame(self, frame):
        if self.frame_stack:
            current_frame = self.frame_stack[-1]
            current_frame.pack_forget()
        frame.pack()
        self.frame_stack.append(frame)

    def go_back(self):
        self.switch_frame(WelcomePage(self))


app = MainApplication()
app.mainloop()
