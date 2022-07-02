class QuizBrain:

    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(
            f"Q.{self.question_no}: {question.text}. (True/False): ").lower()
        self.check_answer(question.answer.lower(), answer)

    def check_answer(self, question_answer, user_answer):
        if user_answer == question_answer:
            self.score += 1
            print("you are correct")

        else:
            print("You're wrong")

        print(f"The correct answer is {question_answer}")
        print(f"your current score = {self.score}/{self.question_no}\n")
