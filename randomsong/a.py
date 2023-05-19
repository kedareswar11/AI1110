import os
import numpy as np
import pygame
import tkinter as tk

# Set the path to the folder containing your music files
music_folder =  "/home/kedareswar/randomsong/playsong"

# Initialize Pygame mixer for playing music
pygame.mixer.init()

# Get a list of all the music files in the folder
music_files = os.listdir(music_folder)

# Shuffle the list of music files randomly using numpy random permutation
shuffled_files = np.random.permutation(music_files)

# Create a function to play the current song
def play_song(index):
    # Load the music file into Pygame mixer
    pygame.mixer.music.load(os.path.join(music_folder, shuffled_files[index]))

    # Play the music file
    pygame.mixer.music.play()

# Create a function to play the next song
def play_next_song(event=None):
    # Get the index of the current song in the shuffled list
    index = current_song_var.get()

    # Increment the index to play the next song
    index += 1

    # Check if all songs have been played
    if index >= len(shuffled_files):
        # Show a message when all songs have been played
        current_song_var.set("All songs played. Thank you!")
        return

    # Update the current song index variable
    current_song_var.set(index)

    # Play the next song
    play_song(index)

# Create the main UI window
window = tk.Tk()

# Set the title of the window
window.title("Music Player")

# Create a label for the current song
current_song_var = tk.IntVar()
current_song_label = tk.Label(window, textvariable=current_song_var)
current_song_label.pack()

# Create a next button
next_button = tk.Button(window, text="Next", command=play_next_song)
next_button.pack()

# Configure Pygame to generate an event when the music finishes playing
pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Bind the end event to the play_next_song function
window.bind(pygame.USEREVENT, play_next_song)

# Play the first song
play_song(0)

# Start the UI event loop
window.mainloop()
