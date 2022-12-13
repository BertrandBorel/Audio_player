# Audio player with Python and Tkinter

# You need to change the 'path' : put your music path. 
# -----------------------------------------------------------------------------

# Importations
import os
from tkinter import *
from PIL import ImageTk, Image
# for sound : 
from pygame import mixer


# Instantiate mixer
mixer.init()

# music path 
# ----------------------------
# change here :
path = "your path"
# ----------------------------
file = os.listdir(path)

# retrieve song names
names = []
for music in file :
    # delete extension '.mp3'
    n = music
    extensions = ['.mp3']
    for ext in extensions:
        n = n.replace(ext, "")
        names.append(n)


# Tkinter
root = Tk()
root.title("Audio player")

# value, 0 or 1 for play or pause
value = 0
# index for the song names
index = 0

# insert an image
canvas = Canvas(root, width = 300, height = 300) 
canvas.grid(row=0, column=1)
img = ImageTk.PhotoImage(Image.open("./image.jpg").resize((300, 300)))    
canvas.create_image(20,20, anchor=NW, image=img)

# music title
title = Label(root, text=names[index])
title.grid(row=1, column=1)

# function : play the sound
def play():
    global path, index, value
    if value == 0 :
        mixer.music.load(path + file[index])   
        mixer.music.play()
        value = 1
    else :
        mixer.music.unpause()	
        value = 0

# function : pause the song
def stop():
    global value
    mixer.music.pause()	
    value = 1

# function : next song
def next():
    global index, button_next
    mixer.music.load(path + file[index])
    mixer.music.play()
    if index == len(file)-1:
        button_next = Button(root, text=">>", command=next, state=DISABLED)
    else :
        index += 1
    title["text"]= names[index]

# function : previous song
def back():
    global index, button_before
    mixer.music.load(path + file[index])
    mixer.music.play()
    if index == 0:
        button_before = Button(root, text="<<", command=next, state=DISABLED)
    else :
        index -= 1
    title["text"]= names[index]


# buttons 
button_play = Button(root, text="Play", command=play)
button_play.grid(row=0, column=2)

button_pause = Button(root, text="pause", command=stop)
button_pause.grid(row=0, column=3 )


button_before = Button(root, text="<<", command=back)
button_before.grid(row=1, column=0)

button_next = Button(root, text=">>", command=next)
button_next.grid(row=1, column=3)

# display
root.mainloop()