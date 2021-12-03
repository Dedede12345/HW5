
FAMILY = ('Me', 'Bro', ('Dad', ('Grandma', 'grandad')), ("Ma", ('grandmother', 'grandfather')))

print(f'Отец матери: {FAMILY[3][1][1]}, мать отца: {FAMILY[2][1][0]}')

def count(a):
    quantity = 0
    for member in a:
        if isinstance(member, str):
            quantity += 1
        elif isinstance(member, tuple):
            for meme in member:
                if isinstance(meme, str):
                    quantity += 1
                elif isinstance(meme, tuple):
                    for mememe in meme:
                        if isinstance(mememe, str):
                            quantity += 1
                        elif isinstance(mememe, tuple):
                            for memememe in mememe:
                                if isinstance(memememe, str):
                                    quantity +=1


    print(f'Всего в семье {quantity} членов.')

count(FAMILY)

grandchildren = ('Izya','Moysha')

siblings = (grandchildren, FAMILY)

count(siblings)

input('Для выхода нажмите \'enter\'')
