class QuizBrain:
    # Constructor
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Checks whether there are questions left in the list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Returns the next question in the list"""
        current_question = self.question_list[self.question_number] # Get the current question object using the index(question number) in the list, question_list
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer) # uses method check_answer

    def check_answer(self,user_answer,correct_answer):
        """Checks whether the answer input by user is the correct answer"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.\nThe correct answer was {correct_answer}")

        print(f"Your current score is {self.score}/{self.question_number}")
        print()
