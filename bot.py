import random

program_name = 'Chat Bot Program'

def ask_question(question):
    while True:
        answer = input(question + '')
        if not answer:
            print('Please enter your answer.')
        else:
            break
    return answer


def general_computer_response():
    return random.choice([
        'That\'s  very intersting. Tell me more?',
        'Really? How did that happen?',
        'Why do you think that is? ',
        'No way! And then what?',
        'What makes you say that? ',
        'How did you come to that conclusion?'
        'Can you elaborate on that?',
        'I\'d like to hear mnore about it? ',
        'Please tell me more',
        'So hoe did you feel about that?',
        'What will you do next?'
    ])