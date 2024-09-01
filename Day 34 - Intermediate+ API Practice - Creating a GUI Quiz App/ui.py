from tkinter import *

THEME_COLOR = "#375362"


class Ui:
    def __init__(self, quiz_list):
        self.quiz_brain = quiz_list

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=10, pady=10)
        self.window.title("Quizzer")

        self.score = Label(text=f"Score: {self.quiz_brain.score}", bg=THEME_COLOR, fg="White")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=320, height=340)
        self.question = self.canvas.create_text(160, 170, font=("Ariel", 20, "italic"), width=320, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true = PhotoImage(file="./images/true.png")

        self.true_button = Button(image=self.true, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        self.false = PhotoImage(file="./images/false.png")

        self.false_button = Button(image=self.false, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")

        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz_brain.next_question())
        else:
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_answer(self):
        if self.quiz_brain.check_answer("True"):
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.next_question)

    def false_answer(self):
        if self.quiz_brain.check_answer("False"):
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.next_question)
