from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

no_of_questions = len(question_data)

question_bank = []
for data in question_data:
    text = data["text"]
    answer = data["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()
print("you've completed the quiz")
print(f"your final score was: {quizbrain.score}/{quizbrain.question_no}")
