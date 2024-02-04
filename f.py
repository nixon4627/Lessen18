def is_logic():
    if 2>1:
        return True
    else:
        return False
if is_logic():
    print('Все хорошо')

def in_logic():
    return 2>1

if 2>1:
    print('Все хорошо')

if(True if 2 > 1 else False) == True:
    print('Все хорошо')
