class Question():
    def __init__(self, ids, question, options):
        self.ids = ids
        self.question = question
        self.options = options
        
    def answer(self, ans):
        return self.options[ans]

class Quiz():
    def __init__(self):
        self.memory = dict()
        
    def add_question(self, question_class):
        self.memory[question_class.ids] = question_class
        
    def execute_question(self, question_id):
        print(f"{self.memory[question_id].question}")
        print("-"*20)
        for pos, option in enumerate(self.memory[question_id].options):
            print(f"{pos+1} | {option}")
        print("-"*20)
        try:
            user_input = int(input(">> "))
        
            options = list(self.memory[question_id].options)
            result = self.memory[question_id].answer(options[user_input-1])
            return "Correct" if result else "Incorrect"
        except ValueError:
            return "Incorrect notation, please use the integers on the side..."
        

if __name__ == "__main__":
    quiz1 = Quiz()
    
    question1 = Question(1, "How are you?", {"Good": True, "Bad": False})
    question2 = Question(2, "Which person is the best to hang out with?", {"Myself": True, "Timmy": False, "Jacob": False})
    quiz1.add_question(question1)
    quiz1.add_question(question2)
    
    result = quiz1.execute_question(2)
    
    print(result)
