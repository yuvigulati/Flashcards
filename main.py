import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Arial", 40, "italic")

# Read the CSV file into a DataFrame
df = pandas.read_csv("data/french_words.csv")
data_list = df.to_dict(orient='records')

# ----------------------------------GENERATING RANDOM NUMBER USING THE BUTTONS--------------------------------
num = 0
french_word = data_list[num]["French"]
english_word = data_list[num]["English"]

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def english_canvas():
    global french_word, english_word
    canvas.itemconfigure(canvas_images, image=new_image)
    canvas.grid(column=1, row=0)
    language_label.config(text="English", bg="#91C2AF", fg="white", font=FONT)
    language_label.place(x=300, y=150)

    word_label.config(text=english_word, bg="#91C2AF", fg="white", font=("Arial", 60, "bold"))
    word_label.place(x=280, y=250)


def saving_data():
    global french_word, english_word
    with open("words_to_learn.csv", mode="a") as file:
        file.write(f"{french_word}, {english_word}\n")


def new_word():
    global num, french_word, english_word
    num += 1
    french_word = data_list[num]["French"]
    english_word = data_list[num]["English"]
    flashcard()
    saving_data()
    data_list.remove(french_word)
    data_list.remove(english_word)


def previous_word():
    global num, french_word, english_word
    num -= 1
    french_word = data_list[num]["French"]
    english_word = data_list[num]["English"]
    flashcard()


def flashcard():
    global old_image, new_image, french_word, english_word, canvas, canvas_images, \
        language_label, word_label, my_image, image_2

    canvas = Canvas(width=830, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
    old_image = PhotoImage(file="images/card_front.png")
    new_image = PhotoImage(file="images/card_back.png")
    canvas_images = canvas.create_image(415, 300, image=old_image)
    canvas.grid(column=1, row=0)

    language_label = Label(text="French", bg="white", font=FONT)
    language_label.place(x=300, y=150)

    word_label = Label(text=french_word, bg="white", font=("Arial", 60, "bold"))
    word_label.place(x=280, y=250)

    window.after(5000, english_canvas)

    my_image = PhotoImage(file="images/right.png")
    image_2 = PhotoImage(file="images/wrong.png")
    right_button = Button(image=my_image, highlightthickness=0, command=new_word)
    right_button.place(x=500, y=575)
    wrong_button = Button(image=image_2, highlightthickness=0, command=previous_word)
    wrong_button.place(x=200, y=575)


saving_data()
flashcard()


window.mainloop()
