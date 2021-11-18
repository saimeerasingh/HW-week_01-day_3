
guess_quiz = input('Guess where did Python get its name from? ')

def guess_the_answer(guess_quiz):
    if guess_quiz == 'Monty Python':
        return "Yayy! thats correct :)"
    else:
        return "Correct answer : Monty Python!"
print(guess_the_answer(guess_quiz))