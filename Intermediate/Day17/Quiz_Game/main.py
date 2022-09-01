from data import *
from question_model import *
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


qb = QuizBrain(question_bank)
while qb.still_has_questions():
    quest = question_bank[qb.question_number]
    answer = qb.next_question()
    qb.check_answer(quest.correct_answer, answer)

qb.final_score()
