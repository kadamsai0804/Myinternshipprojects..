class Question:
    def _init_(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
    
    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()


class Quiz:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            question.display_question()
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()

        print(f"You scored {self.score}/{len(self.questions)}")


# Sample questions
question1 = Question("What is the capital of India?",
                     ["Mumbai", "New Delhi", "Hyderabad", "Banglore"], "New Delhi")
question2 = Question("Which planet is known as the Red Planet?",
                     ["Mars", "Venus", "Jupiter", "Saturn"], "Mars")
question3 = Question("What is the chemical symbol for Gulcose?",
                     ["H2O", "CO2", "O2", "C6H12O6"], "C6H12O6")

questions = [question1, question2, question3]

# Create quiz object and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()