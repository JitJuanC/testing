from drawing import hangman_pic

start_no = 1
pointer = 0
chances = 12
placed_answer = input('Welcome to the Hangman Game MUAHAHAHAH! What word do you want your victim to guess? \n')
answer = placed_answer.lower().strip()
category = input('What category is it? \n')
user_answer = ''
guess = ''
drawn = 1

while start_no < chances:
    print('Category: ' + category.strip())
    print('Your current answer is = ' + user_answer)
    hangman_pic(drawn)
    print('Your wrong guesses = ' + guess)
    user_input = input('What is the next letter? :').lower().strip()
    while len(user_input) > 1:
        print('Please only provide one alphabet, guess again!')
        break
    else:
        if user_input == answer[pointer]:
            print('CORRECT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            user_answer += answer[pointer]
            pointer += 1
            if len(user_answer) is len(answer):
                print('Congratulations you have won!!!!!!!!!! :)')
                start_no = 12
                break
            else:
                continue
        else:
            drawn += 1
            print('WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            guess += user_input[0]
        start_no += 1
