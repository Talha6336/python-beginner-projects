import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'


def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)
    return input('Your answer: ').upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)
    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            cprint("Correct", 'green')
            score += 1
        else:
            cprint(f'Wrong! The correct answer is {item[ANSWER]}', 'red')

    cprint(
        f'Quiz over! Your final score is {score} out of {len(quiz)} ', 'green')


def main():
    quiz = [
        {
            QUESTION: 'What is the capital of Pakistan?',
            OPTIONS: ['A. Lahore', 'B. Islamabad', 'C. Karachi', 'D. Faisalabad'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'Which planet is known as red planet ?',
            OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'What is the largest ocean on Earth?',
            OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
            ANSWER: 'D'
        }
    ]
    run_quiz(quiz)


if __name__ == '__main__':
    main()
