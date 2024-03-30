import cv2
import threading
from tkinter import Canvas
from appSettings import AppSettings
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, pl_video, video_path, master, size):
        self.pl_video = pl_video
        self.video_path = video_path
        self.master = master
        self.canvas = Canvas(master, width=size[0], height=size[1])
        self.pause = False

        if self.pl_video == 1:
            self.stream = cv2.VideoCapture(self.video_path)
        else:
            self.stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            self.update()

    def place(self, relx, rely):
        self.canvas.place(relx=relx, rely=rely)
        self.update()

    def update(self):
    try:
        ret, frame = self.stream.read()

        if ret:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            if not self.pause:
                self.master.after(15, self.update)
        else:
            self.stream.release()
    except Exception as g:
        print("no stream")


    def place_forget(self):
        self.canvas.place_forget()
        self.pause_video()
        self.stream.release()

    def pause_video(self):
        self.pause = True