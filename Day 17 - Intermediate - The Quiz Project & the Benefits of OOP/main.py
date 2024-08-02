from question_model import QuestionModel
from quiz_brain import QuizBrain

question_model = QuestionModel()
quiz_brain = QuizBrain()

while question_model.random_question():
    quiz_brain.print_question(question_model)
    user_answer = input().capitalize()
    if user_answer == "Quit":
        break
    quiz_brain.check_answer(user_answer, question_model)

print(f"Quiz finished! Your final score is: {quiz_brain.true}/{quiz_brain.num}")
