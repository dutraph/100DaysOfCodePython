from data import *
from question_model import *
from quiz_brain import QuizBrain
import os


def cls():
    os.system('cls')

# rand_data = choice(question_data)
# question = Question(rand_data['text'], rand_data['answer'])


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


qb = QuizBrain(question_bank)
while qb.still_has_questions():
    quest = question_bank[qb.question_number]
    answer = qb.next_question()
    if quest.answer == answer.title():
        qb.score_on()

print(f"Your Score is {qb.score}")


# print(question_bank[0].answer)
#
# print(question.text)
# print(question.answer)