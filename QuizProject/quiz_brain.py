class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.list = list
        self.score = 0

    def next_question(self):
        number = self.question_number
        question = self.list[number]
        user_answer = input(f"Q.{number}: {question.question} (True/False)?")
        self.check_answer(user_answer, question.answer)


    def still_has_question(self):
        number_of_question = len(self.list) - 1
        what_question = self.question_number
        if what_question < number_of_question:
            self.question_number += 1
            return True

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right")
            self.score+= 1
        else:
            print("That's wrong.")
        print(f"The Correct answer was {question_answer}")
        print(f"Your current Score {self.score}/{self.question_number + 1}")
        print()

