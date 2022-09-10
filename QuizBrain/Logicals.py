class Quiz:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def question_(self):
        try:
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.q_text}: ")
            self.answer_check(user_answer, current_question.q_answer)
            return True

        except IndexError:
            print(f"You scored {self.score}")
            quit()

    def answer_check(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        if user_answer == 'exit':
            print(f"You scored {self.score}.")
            quit()
        else:
            pass
        print(f"your current score is {self.score} / {self.question_number}")



