class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer

new_q = Question("Computer is a Machine", "True")

print(new_q.text)