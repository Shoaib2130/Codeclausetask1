import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("500x400")
        self.configure(bg="#D7BDE2")  # Set background color

        # Initialize Pygame mixer
        pygame.mixer.init()

        self.current_track = None
        self.playlist = []

        # Load a default album cover image
        self.album_cover_image = Image.open(r"C:/Users/DELL/Downloads/download.jpg")
        self.album_cover_image = self.album_cover_image.resize((300, 300), Image.Resampling.LANCZOS)
        self.album_cover_image = ImageTk.PhotoImage(self.album_cover_image)

        self.create_widgets()

    def create_widgets(self):
        # Album cover image
        self.album_cover_label = tk.Label(self, image=self.album_cover_image, bg="#D7BDE2")
        self.album_cover_label.pack(pady=10)

        # Track label
        self.track_label = tk.Label(self, text="No Track Selected", font=("Helvetica", 12), bg="#D7BDE2", fg="black")
        self.track_label.pack()

        # Buttons
        self.button_frame = tk.Frame(self, bg="#D7BDE2")
        self.button_frame.pack()

        self.btn_load = tk.Button(self.button_frame, text="Load Track", command=self.load_track)
        self.btn_load.pack(side=tk.LEFT, padx=5)

        self.btn_play = tk.Button(self.button_frame, text="Play", command=self.play_track, state=tk.DISABLED)
        self.btn_play.pack(side=tk.LEFT, padx=5)

        self.btn_pause = tk.Button(self.button_frame, text="Pause", command=self.pause_track, state=tk.DISABLED)
        self.btn_pause.pack(side=tk.LEFT, padx=5)

        self.btn_stop = tk.Button(self.button_frame, text="Stop", command=self.stop_track, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        self.btn_quit = tk.Button(self.button_frame, text="Quit", command=self.quit)
        self.btn_quit.pack(side=tk.LEFT, padx=5)

    def load_track(self):
        track_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])

        if track_path:
            self.playlist.append(track_path)
            self.current_track = len(self.playlist) - 1

            # Display album cover if available
            self.display_album_cover(track_path)

            # Update track label and enable buttons
            self.track_label.config(text=os.path.basename(track_path))
            self.btn_play.config(state=tk.NORMAL)
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.NORMAL)

    def play_track(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause_track(self):
        if pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() > 0:
                pygame.mixer.music.pause()

    def stop_track(self):
        pygame.mixer.music.stop()

    def display_album_cover(self, track_path):
        # Your code to extract album cover from track metadata and display it
        # For this example, we'll use a default image
        self.album_cover_image = Image.open("default_album_cover.png")
        self.album_cover_image = self.album_cover_image.resize((150, 150), Image.ANTIALIAS)
        self.album_cover_image = ImageTk.PhotoImage(self.album_cover_image)
        self.album_cover_label.config(image=self.album_cover_image)

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
