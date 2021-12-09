answer = 'Минск'

end = answer[-1]

print(f'Начальный город: {answer}')

forbidden = ['й', 'ь', 'ъ']

while True:
    answer = input(f'Введите город начинающийся с \'{end}\' ').casefold()

    if answer == 'сдаюсь':
        break

    for i in forbidden:
        answer = answer.replace(i, '')
    if answer[0] == end:
        end = answer[-1]
        continue
    else:
        print('Попробуйте ввести еще раз или введите \'сдаюсь\'\n (С любым регистром!!!)')

print('Спасибо за игру!')
