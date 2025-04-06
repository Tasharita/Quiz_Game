from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Loops through each question in the question_data list from class data
for question in question_data:
    question_text = question["text"]  # Extracts the text of question
    question_answer = question["answer"]  # Extracts answer of the question
    new_question = Question(question_text,question_answer) # Creates a new Question object
    question_bank.append(new_question) # adds the object to the question_bank list

quiz = QuizBrain(question_bank) # Create a QuizBrain object with the list of Question objects

# Checks whether there are still questions left using a method from QuizBrain class
while quiz.still_has_questions():
    quiz.next_question() # Call the method to display the next question and get user input

print(f"You've completed the quiz\nYour final score was {quiz.score}/{quiz.question_number}")
