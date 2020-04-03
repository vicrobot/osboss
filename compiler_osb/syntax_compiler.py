KEYWORDS = ['is', 'show']
OPERATORS = ['+', '-']

def parsed(line):
    main_l  = [i.strip() for i in line.split(' ') if i.strip()]
    pycode = ''
    for j,i in enumerate(main_l):
        if i in KEYWORDS:
            if i == 'is':
                temp = parsed(" ".join(main_l[j+1:]))
                pycode += f'{main_l[j-1]} = {temp}'
                break
            elif i == 'show':
                pycode += f'print({parsed(" ".join(main_l[j+1:]))})'
                break
        elif i in OPERATORS:
            if i == '+':
                pycode += f'{main_l[j-1]} + {parsed(" ".join(main_l[j+1:]))}'
                break
            elif i == '-':
                pycode += f'{main_l[j-1]} - {parsed(" ".join(main_l[j+1:]))}'
                break
    ret =  pycode if pycode else ' '.join(main_l)
    return ret

def osbtopy(lines_list):
    pycode = ''
    for line in lines_list:
        pycode += parsed(line)
        pycode += '\n'
    return pycode
                
