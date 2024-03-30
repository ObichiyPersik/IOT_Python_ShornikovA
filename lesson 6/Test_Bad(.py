import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Toplevel
from PIL import Image, ImageTk
import time
import os
import threading
from appSettings import pl_video, video_path

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Анализ видео")
        self.play_button = ttk.Button(self, text="Старт/Пауза", command=self.play_pause)
        self.play_button.place(x=10, y=10)
        self.screenshot_button = ttk.Button(self, text="Сделать скриншот", command=self.take_photo)
        self.screenshot_button.place(x=100, y=10)
        self.settings_button = ttk.Button(self, text = "Настройки", command=self.open_settings)
        self.settings_button.place(x=200, y=10)
        self.video_canvas = Canvas(self, width=640, height=480)
        self.video_canvas.place(x=10, y=50)
        self.video_player = VideoPlayer(self, pl_video, video_path,(640, 480))

    def play_pause(self):
        self.video_player.play_pause()

    def take_photo(self):
        self.video_player.take_photo()

    def open_settings(self):
        settings_window = Settings(pl_video, video_path)
        self.wait_window(settings_window)

class Settings(Toplevel):
    def __init__ (self, pl_video, video_path):
        super().__init__()
        self.title("Настройки")
        self.pl_video = pl_video
        self.video_path = video_path

        self.pl_video_var = tk.IntVar(value=self.pl_video)
        self.video_path_var = tk.StringVar(value=self.video_path)

        pl_video_label = ttk.Label(self, text="PL Video:")
        pl_video_label.grid(row=0,column=0, sticky="w")
        self.pl_video_entry = ttk.Entry(self, textvariable=self.pl_video_var)
        self.pl_video_entry.grid(row=0, column=1, sticky="w")

        video_path_label = ttk.Label(self, text="Путь до видео:")
        video_path_label.grid(row=1, column=0, sticky="w")
        self.video_path_entry = ttk.Entry(self, textvariable=self.video_path_var)
        self.video_path_entry.grid(row=1, column=1, sticky="w")

        save_button = ttk.Button(self, text="Сохранить", command=self.save_settings)
        save_button.grid(row=2, columnspan=2)

    def save_settings(self):
        self.pl_video = self.pl_video_var.get()
        self.video_path = self.video_path_var.get()
        self.destroy()

class VideoPlayer:
    def __init__(self, pl_video, video_path, master, size):
        self.stream = cv2.VideoCapture(video_path if pl_video else 0, cv2.CAP_DSHOW)
        self.master = master
        self.canvas = master.video_canvas
        self.pause = False
        self.size = size
        self.place()

    def place(self):
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        self.update()

    def update(self):
        ret, frame = self.stream.read()
        if ret and not self.pause:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, self.size)
            photo = self.convert_frame_to_photo(frame)
            self.canvas.create_image(0,0, anchor="nw", image=photo)
            self.canvas.image = photo
            self.canvas.after(10, self.update)
        else:
            self.pause_video()
            self.stream.release()

    def convert_frame_to_photo(selfself, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)
        return photo

    def pause_video(self):
        self.pause = True

    def play_pause(self):
        self.pause = not self.pause
        if not self.pause:
            self.update()

    def take_photo(self):
        screenshot_thread = threading.Thread(target=self.find_in_stream)
        screenshot_thread.start()

    def find_in_stream(self):
        os.makedirs("screenshots", exist_ok=True)
        while not self.pause:
            ret, frame = self.stream.read()
            if ret:
                cv2.imwrite(f"screenshots/screenshot_{time.time()}.jpg", frame)
            time.sleep(0.5)

root = MainWindow()
root.mainloop()