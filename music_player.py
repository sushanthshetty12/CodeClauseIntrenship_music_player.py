import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        
        pygame.mixer.init()
        self.music_files = []
        self.current_index = 0
        
        self.label = tk.Label(root, text="Select a folder to play music", wraplength=300)
        self.label.pack(pady=20)
        
        self.select_button = tk.Button(root, text="Select Folder", command=self.load_music)
        self.select_button.pack()
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()
        
        self.pause_button = tk.Button(root, text="Pause/Resume", command=self.pause_music)
        self.pause_button.pack()
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()
        
    def load_music(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.music_files = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith(".mp3")]
            self.current_index = 0
            if self.music_files:
                self.label.config(text=f"Loaded {len(self.music_files)} songs")
            else:
                self.label.config(text="No music files found in the folder")

    def play_music(self):
        if self.music_files:
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()
            self.label.config(text=f"Playing: {os.path.basename(self.music_files[self.current_index])}")
    
    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.label.config(text="Music stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()