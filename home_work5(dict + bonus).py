# price = ('price', 'cost')

product = {'name':'Apple',
           ('price', 'cost') :'3.00 $',
           'weight':'176 gr.',
           'quantity': 5}

print(product[('price', 'cost')])

numbers_A_to_R = {3 : 'III',
             15 : 'XV',
             10 : 'X'}

ino = []

for keys, values in numbers_A_to_R.items():
    ino.append(keys)

x = 0

for i in range(len(ino)):
    if ino[i] > x:
        x = ino[i]
        ino[0],  ino[i] = ino[i],  ino[0]
    elif ino[i] > ino[1]:
        ino[i], ino[1] = ino[1], ino[i]
    else:
        pass

for i in ino:
    print(i, end=' ')

print()

for i in numbers_A_to_R:
    print(numbers_A_to_R[i], end=' ')

print()

year_of_birth = {2006 : '50 48 48 54 '}

print(year_of_birth[2006])

# a = '0o131'

x = 0

lis = ['0o131', '0o157', '0o165', '0o40', '0o141', '0o162', '0o145', '0o40', '0o147', '0o145', '0o156', '0o151', '0o165', '0o163', '0o41']

lis0 = []

def deoct(oct):
    g = 0
    for i in range(len(oct) - 2):
        x =int(oct[-(i + 1)]) * (8 ** i)
        g += x
    return g

for u in lis:
    lis0.append(deoct(u))

print(lis0)
