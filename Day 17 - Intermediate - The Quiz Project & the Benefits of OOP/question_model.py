from data import question_data
import random


class QuestionModel:
    def __init__(self):
        self.questions = question_data
        self.question = ""
        self.answer = ""

    def random_question(self):
        if self.questions:
            selected_question = random.choice(self.questions)
            self.question = selected_question["text"]
            self.answer = selected_question["answer"]
            self.questions.pop(self.questions.index(selected_question))
            return True

        return False
