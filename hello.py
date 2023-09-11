def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if(b==0):
        return a
    return a / b

while(1):
    cmd = input("수식 입력 : (usage: 2 + 3)> ")
    if cmd == 'end':
        break
    cmds = cmd.split(' ')
    # @ToDo 
    a , b, c = int(cmds[0]), cmds[1], int(cmds[2])

    if b == '+':
        r = plus(a, c)
    elif b == '-':
        r = min(a, c)
    elif b == '*':
        r = mul(a, c)
    elif b == '/':
        r = div(a, c)
    
    if b in ['+', '-', '*']:
        print("Answer is {:d}".format(r))
    else:
        print("Answer is {:.2f}".format(r))