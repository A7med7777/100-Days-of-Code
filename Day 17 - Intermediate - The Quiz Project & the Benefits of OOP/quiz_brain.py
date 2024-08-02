class QuizBrain:
    def __init__(self):
        self.true = 0
        self.num = 0

    def check_answer(self, answer, question):
        if answer == question.answer:
            print("You got it right!")
            self.true += 1
        else:
            print("That's wrong!")

        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.true}/{self.num}")
        print()

    def print_question(self, question_txt):
        self.num += 1
        print(f"Q.{self.num}: {question_txt.question} (True/False)?: ", end="")
