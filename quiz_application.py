# -*- coding: utf-8 -*-
"""quiz application

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IJNBY28AyNKmyK8fXMiBDPBzFze5AL9t
"""



class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == question.answer.strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")

    print(f"You got {score}/{len(questions)} questions right.")

def main():
    print("Welcome to the Quiz Application!\n")

    # Define quiz questions
    question_prompts = [
        "What is the chemical symbol for water??\n(a) H2O\n(b) CO2\n(c) O2\n",
        "The Great Wall of China was primarily built to protect against invasions from which group?\n(a) Mongols\n(b) Romans\n(c) Egyptians\n",
        "Who wrote 'Romeo and Juliet'?\n(a) Charles Dickens\n(b) William Shakespeare\n(c) J.K. Rowling\n",
        "What is the capital of France?\n(a) London\n(b) Berlin\n(c) Paris\n",
        "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n"
    ]

    # Correct answers
    answers = ["a", "a", "b", "c", "b"]

    # Create list of Question objects
    questions = [Question(prompt, answer) for prompt, answer in zip(question_prompts, answers)]

    # Run the quiz
    run_quiz(questions)

if __name__ == "__main__":
    main()