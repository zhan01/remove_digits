import re
string = 'Alice is 21 years old'


def nodigits(string):
    pattern = '\d'
    nodigit_list = re.sub(pattern, '', string)
    
    return nodigit_list

print(nodigits(string))
assert nodigits(string) == 'Alice is  years old'
assert nodigits('3 times a day he drinks 2 liters of water') == ' times a day he drinks  liters of water'
assert nodigits('Bob is 30 years old and have 3 cats') == 'Bob is  years old and have  cats'


