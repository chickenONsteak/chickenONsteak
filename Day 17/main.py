from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Test comment
question_bank = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
