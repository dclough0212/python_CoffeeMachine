class QuizBrain():
  answer = ""
  def __init__(self, questions):
    self.question_list = questions
    self.question_number = 1
    self.score = 0;

  def still_has_questions(self):
    return self.question_number <= len(self.question_list)

  def next_question(self):
    question = self.question_list[self.question_number-1]
    
    self.answer = input(f"Q{self.question_number}: {question.text}")
    if (self.answer.lower() == question.answer.lower()):
      print("Correct!")
      self.score += 1
      
    else:
      print("IDIOT!")  
    
    print(f"{self.score} out of {self.question_number} correct")
    self.question_number += 1      