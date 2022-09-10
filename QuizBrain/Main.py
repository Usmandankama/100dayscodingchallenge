from Data import *
from Logicals import *


class Question:

    def __init__(self,q_text,q_answer):
        self.q_text = q_text
        self.q_answer = q_answer

question_bank = []
for question in questions:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz = Quiz(question_bank)
while True:
    quiz.question_()
# to stop the quiz and get your score printed type exit
