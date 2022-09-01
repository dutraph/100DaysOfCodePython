class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.question} (True/False): ")

    def score_on(self):
        self.score += 1

    def check_answer(self, question, answer):
        if question == answer.title():
            self.score_on()
            print("You got it right")
            print(f"Your current score is: {self.score}/{self.question_number}", end='\n\n')
        else:
            print("You got it wrong")
            print(f"Your current score is: {self.score}/{self.question_number}", end='\n\n')

    def final_score(self):
        print("You've completed the quiz...")
        print(f"Your final score is: {self.score}/{self.question_number}")