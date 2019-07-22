import re
string = 'Alice is 21 years old'


def nodigits(string):
    pattern = '\d'
    nodigit_list = re.split(pattern, string)
    result = ' '.join(nodigit_list)
    print(result.replace('    ',' '))
    return result


assert nodigits(string) == 'Alice is    years old'
assert nodigits('10 days she had to attend school') == '   days she had to attend school'
assert nodigits('John is 18 years old and he has 5 cats') == 'John is    years old and he has   cats'
assert nodigits('We are going to buy 10 orenges from 5 different shops') == 'We are going to buy    orenges from   different shops'