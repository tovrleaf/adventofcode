import os

def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

cur = ''
passports = []
for l in get_input():
    if l == '':
        passports.append(cur.strip())
        cur = ''
        continue
    cur += ' ' + l
passports.append(cur.strip())


keys = []
for l in passports:
    tokens = [t.split(':')[0] for t in l.split()]
    'cid' in tokens and tokens.remove('cid')
    keys.append(tokens)

required_fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
print(sum([len(set(required_fields).intersection(l)) == len(required_fields) for l in keys]))
