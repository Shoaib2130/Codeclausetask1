import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("400x150")

        # Initialize Pygame mixer
        pygame.mixer.init()

        self.current_track = None
        self.playlist = []

        self.create_widgets()

    def create_widgets(self):
        # Track label
        self.track_label = tk.Label(self, text="No Track Selected", font=("Helvetica", 12))
        self.track_label.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(self)
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

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
