from tkinter import filedialog
from tkinter import *
import pygame
import os
# initialize program variables
root = Tk()
root.title('Music Player')
root.geometry("500x300")

# initialize program
pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

# load music

songs = []
current_song = ""
paused = False

# functions


def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]


def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        pause = False


def pause_music():
    global pause

    pygame.mixer.music.pause()
    paused = True


def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.select_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


def previous_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.select_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

# Images path
script_path = os.path.dirname(os.path.abspath(__file__))
image_play_path = os.path.join(script_path, 'Images', 'Play.png')
image_pause_path = os.path.join(script_path, 'Images', 'Pause.png')
image_next_path = os.path.join(script_path, 'Images', 'Next.png')
image_previous_path = os.path.join(script_path, 'Images', 'Previous.png')

# adding a box for our songs
songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_button_image = PhotoImage(file=image_play_path)
pause_button_image = PhotoImage(file=image_pause_path)
next_button_image = PhotoImage(file=image_next_path)
previous_button_image = PhotoImage(file=image_previous_path)

# creating frame
control_frame = Frame(root)
control_frame.pack()

# buttons
play_button = Button(control_frame, image=play_button_image,
                     borderwidth=0, command=play_music)
pause_button = Button(control_frame, image=pause_button_image,
                      borderwidth=0, command=pause_music)
next_button = Button(control_frame, image=next_button_image,
                     borderwidth=0, command=next_music)
previous_button = Button(
    control_frame, image=previous_button_image, borderwidth=0, command=previous_music)

play_button.grid(row=0, column=1, padx=7, pady=10)
pause_button.grid(row=0, column=2, padx=7, pady=10)
next_button.grid(row=0, column=3, padx=7, pady=10)
previous_button.grid(row=0, column=4, padx=7, pady=10)

# open the window
root.mainloop()
