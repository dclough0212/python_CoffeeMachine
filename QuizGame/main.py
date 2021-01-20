from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for n in question_data:
  question_bank.append(Question(n["text"], n["answer"]))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
  qb.next_question()
