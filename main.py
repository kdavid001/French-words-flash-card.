import csv

import pandas

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random as random

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
random_pair = {}
words = {}

try:
    data = pd.read_csv("data/words to learn")

except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    words = (original_data.to_dict(orient="records"))

else:
    words = (data.to_dict(orient="records"))


def next_card():
    global random_pair, flip_timer
    random_pair = random.choice(words)
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(Title, text="French", fill='black')
    canvas.itemconfig(word, text=random_pair['French'], fill='black')
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(word, text=random_pair['English'], fill="white")


def right():
    words.remove(random_pair)
    next_card()
    data = pandas.DataFrame(words)
    print(words)
    data.to_csv("data/words to learn", index=False)


window.after(3000, func=next_card)

old_image = PhotoImage(file="card_front.png")
new_image = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=old_image)
Title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=right)
right_button.grid(column=1, row=1)

window.mainloop()
