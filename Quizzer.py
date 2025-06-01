import random
import time
import sys
import os

class PythonQuiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.questions = [
            {
                "question": "What does the 'yield' keyword do in Python?",
                "options": [
                    "A) It pauses a function saving its state and returns a value",
                    "B) It terminates a function immediately",
                    "C) It skips the current iteration of a loop",
                    "D) It imports modules dynamically"
                ],
                "answer": "A",
                "explanation": "The 'yield' keyword transforms a function into a generator, which pauses execution and returns a value while saving its state for the next call."
            },
            {
                "question": "Which of these is NOT a valid method for list comprehension filtering?",
                "options": [
                    "A) [x for x in range(10) if x % 2 == 0]",
                    "B) [x if x % 2 == 0 else 0 for x in range(10)]", 
                    "C) [x where x % 2 == 0 for x in range(10)]",
                    "D) [x for x in range(10) if x % 2 == 0 if x < 8]"
                ],
                "answer": "C",
                "explanation": "The 'where' keyword is not used in Python list comprehensions. The correct syntax is 'if' for filtering."
            },
            {
                "question": "What is the purpose of the 'with' statement in Python?",
                "options": [
                    "A) Define a new function scope",
                    "B) Create a context manager for resource cleanup",
                    "C) Import specific functions from a module",
                    "D) Define a new exception type"
                ],
                "answer": "B",
                "explanation": "'with' statements are used for context management, ensuring proper acquisition and release of resources (like files) even if exceptions occur."
            },
            {
                "question": "What will be the output of: lambda x, y, z=3: x + y + z",
                "options": [
                    "A) A tuple containing (x, y, z=3)",
                    "B) A function object that adds three arguments with z defaulting to 3",
                    "C) A syntax error",
                    "D) The sum of x, y, and 3"
                ],
                "answer": "B",
                "explanation": "This creates an anonymous function that takes parameters x and y (required) and z (optional with default 3) and returns their sum."
            },
            {
                "question": "Which of the following accurately describes decorators in Python?",
                "options": [
                    "A) Functions that modify class attributes at runtime",
                    "B) Special methods that override operator behavior",
                    "C) Functions that take another function as argument and extend its behavior",
                    "D) Built-in functions for data validation"
                ],
                "answer": "C",
                "explanation": "Decorators are a way to modify or enhance functions without changing their code, by wrapping them with another function."
            },
            {
                "question": "What is the output of: [i for i in range(5) for j in range(3)]",
                "options": [
                    "A) [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]",
                    "B) [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]",
                    "C) [(0, 0), (0, 1), (0, 2), ..., (4, 2)]",
                    "D) [0, 1, 2, 3, 4]"
                ],
                "answer": "A",
                "explanation": "This nested list comprehension repeats each value i from range(5) three times (once for each j in range(3))."
            },
            {
                "question": "What is the difference between __str__ and __repr__ methods?",
                "options": [
                    "A) __str__ is for strings, __repr__ is for integers",
                    "B) __str__ is for end users, __repr__ is for developers and debugging",
                    "C) __str__ is a built-in method, __repr__ must be defined by users",
                    "D) __str__ works with print(), __repr__ doesn't"
                ],
                "answer": "B",
                "explanation": "__str__ returns a human-readable string representation, while __repr__ returns an unambiguous representation typically used for debugging and development."
            },
            {
                "question": "What does the asterisk (*) operator do when used in a function parameter?",
                "options": [
                    "A) Makes the parameter optional",
                    "B) Collects remaining positional arguments into a tuple",
                    "C) Unpacks a collection into separate arguments",
                    "D) Performs exponentiation on the parameter"
                ],
                "answer": "B",
                "explanation": "In a function definition, *args collects any extra positional arguments into a tuple, allowing functions to accept a variable number of arguments."
            },
            {
                "question": "What is a generator expression in Python?",
                "options": [
                    "A) A mathematical function that generates pseudorandom numbers",
                    "B) A list comprehension that creates generators",
                    "C) An expression that returns an iterator similar to list comprehension",
                    "D) A function that generates new classes at runtime"
                ],
                "answer": "C",
                "explanation": "Generator expressions are like list comprehensions but return an iterator that produces values on demand, saving memory for large datasets."
            },
            {
                "question": "What is the purpose of the nonlocal keyword in Python?",
                "options": [
                    "A) To refer to a variable in the nearest enclosing scope that isn't global",
                    "B) To declare a variable that can be accessed outside the function",
                    "C) To prevent a variable from being modified inside a function",
                    "D) To create a variable that persists between function calls"
                ],
                "answer": "A",
                "explanation": "The nonlocal keyword allows you to modify a variable from an outer (but not global) scope in a nested function."
            }
        ]
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_intro(self):
        """Display the quiz introduction."""
        self.clear_screen()
        print("\n" + "=" * 60)
        print("      INTERMEDIATE PYTHON PROGRAMMING QUIZ")
        print("=" * 60)
        print("\nTest your Python knowledge with this intermediate-level quiz!")
        print("\nInstructions:")
        print("- Answer each question by selecting the correct option (A, B, C, or D)")
        print("- You'll receive immediate feedback after each question")
        print("- At the end, you'll get your final score and performance summary")
        print("\nReady to start? Good luck!")
        print("\n" + "=" * 60)
        input("\nPress Enter to begin...")
    
    def display_question(self, question_data):
        """Display a single question with options."""
        self.clear_screen()
        self.total_questions += 1
        
        print(f"\nQuestion {self.total_questions}:")
        print(f"\n{question_data['question']}\n")
        
        for option in question_data['options']:
            print(option)
        
        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Invalid choice! Please enter A, B, C, or D.")
    
    def provide_feedback(self, question_data, user_answer):
        """Provide feedback on the user's answer."""
        correct_answer = question_data['answer']
        if user_answer == correct_answer:
            self.score += 1
            print("\n✓ Correct! Well done!")
        else:
            print(f"\n✗ Incorrect. The correct answer is {correct_answer}.")
        
        print(f"\nExplanation: {question_data['explanation']}")
        input("\nPress Enter to continue...")
    
    def display_final_results(self):
        """Display the final quiz results."""
        self.clear_screen()
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 60)
        print("                 QUIZ COMPLETED!")
        print("=" * 60)
        print(f"\nYour final score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("\nExcellent! You have mastered intermediate Python concepts!")
        elif percentage >= 70:
            print("\nGood job! You have a solid understanding of Python.")
        elif percentage >= 50:
            print("\nNot bad! Keep practicing to improve your Python skills.")
        else:
            print("\nKeep learning! Review the concepts and try again.")
        
        print("\n" + "=" * 60)
    
    def run_quiz(self):
        """Run the complete quiz."""
        self.display_intro()
        
        # Shuffle questions for variety
        random.shuffle(self.questions)
        
        for question_data in self.questions:
            user_answer = self.display_question(question_data)
            self.provide_feedback(question_data, user_answer)
        
        self.display_final_results()


if __name__ == "__main__":
    quiz = PythonQuiz()
    quiz.run_quiz()