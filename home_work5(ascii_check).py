text  = input()
def asciicheck(a):
    assert len(a) == len(a.encode('ascii'))
    print('yes')

asciicheck(text)
