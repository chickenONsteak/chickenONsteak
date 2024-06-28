class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}. {current_question.text} (True/False)?: ").lower()
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_a, correct_a):
        if user_a == correct_a.lower():
            self.score += 1
            print("You are correct!")
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_a}")
        if self.question_num < len(self.question_list):
            print(f"Your current score is {self.score}/{self.question_num}\n")
        else:
            print("You've completed the quiz!")
            print(f"Your final score is {self.score}/{self.question_num}\n")
