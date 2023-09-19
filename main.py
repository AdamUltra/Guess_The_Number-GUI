from tkinter import *
from tkinter import messagebox
from random import randint
inserted_guess = ""
correct_answer = ""


def start():
    global inserted_guess, correct_answer
    inserted_guess = ""
    correct_answer = randint(0, 20)
    print(correct_answer)


WHITE = "white"

win = Tk()
win.config(padx=20, pady=20, bg=WHITE)
win.title("Guess the number")
win.minsize(200, 200)
start()


def check_answer(x):
    global inserted_guess, correct_answer
    inserted_guess = number_entry.get()
    if int(inserted_guess) == correct_answer:
        you_win = messagebox.askyesno("Congrats", "You won!!\nDo you want to play again?")

        if you_win:
            number_entry.delete(0, END)
            start()

        else:
            quit()

    else:
        you_lose = messagebox.askyesno("Hard Luck", f"You lost!!\nThe number was: {correct_answer}\nDo you want to play again?")

        if you_lose:
            number_entry.delete(0, END)
            start()

        else:
            quit()


# Labels
enter_guess = Label(text="Enter your guess: ", bg=WHITE)
enter_guess.grid(column=0, row=0)

# Entry
number_entry = Entry(width=4, borderwidth=2)
number_entry.grid(column=1, row=0)
number_entry.focus_set()

# Button
confirm_button = Button(text="Confirm", command=lambda: check_answer(""))
confirm_button.grid(column=2, row=0)

win.bind("<Return>", check_answer)
win.mainloop()
