import tkinter as tk
import cv2
from PIL import Image, ImageTk
from AppSettings import AppSettings

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pl_video = AppSettings.pl_video
        self.video_path = AppSettings.video_path
        self.title("Main Window")
        self.canvas = tk.Canvas(self, width=800, height=1200)
        self.canvas.pack()
        self.video_player = VideoPlayer(self, 800, 1200)
        self.video_player.place(relx=0, rely=0)
        self.play_button = tk.Button(self, text="Старт/Пауза", command=self.play_pause)
        self.play_button.pack()
        self.photo_button = tk.Button(self, text="Сделать скриншот", command=self.take_photo)
        self.photo_button.pack()
        self.settings_button = tk.Button(self, text="Настройки", command=self.open_settings)
        self.settings_button.pack()

    def play_pause(self):
        self.video_player.play_pause()

    def take_photo(self):
        self.video_player.take_photo()

    def open_settings(self):
        settings_window = Settings(self)
        self.wait_window(settings_window)


class VideoPlayer:
    def __init__(self, master, width, height):
        self.pl_video = master.pl_video
        self.video_path = master.video_path
        self.master = master
        self.width = width
        self.height = height
        self.stream = cv2.VideoCapture(self.video_path if self.pl_video else 0)
        self.canvas = None
        self.pause = False
        self.photo = None
        self.start_frame = 0

    def place(self, relx, rely):
        self.canvas = self.master.canvas
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
                self.stream.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)
                if not self.pause:
                    self.update()
        except Exception as e:
            print("Нет видеопотока")

    def play_pause(self):
        self.pause = not self.pause
        if self.pause:
            self.start_frame = self.stream.get(cv2.CAP_PROP_POS_FRAMES)
            self.stream.release()
        else:
            self.stream.open(self.video_path if self.pl_video else 0)
            self.stream.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)
            self.update()

    def take_photo(self):
        ret, frame = self.stream.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            image.save("photo.png", "PNG")


class Settings(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Настройки")
        self.pl_video_var = tk.IntVar()
        self.pl_video_var.set(master.pl_video)
        self.video_path_var = tk.StringVar()
        self.video_path_var.set(master.video_path)
        self.source_label = tk.Label(self, text="Тип источника:")
        self.source_label.grid(row=0, column=0)
        self.source_combo = tk.OptionMenu(self, self.pl_video_var, 0, 1)
        self.source_combo.grid(row=0, column=1)
        self.path_label = tk.Label(self, text="Путь к видео:")
        self.path_label.grid(row=1, column=0)
        self.path_entry = tk.Entry(self, textvariable=self.video_path_var)
        self.path_entry.grid(row=1, column=1)
