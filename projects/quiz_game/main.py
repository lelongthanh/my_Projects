from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question['text'], question['answer'])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\n")
print("You've completed quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")