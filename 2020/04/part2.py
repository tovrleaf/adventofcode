import os
import re

def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

cur = ''
rows = []
for l in get_input():
    if l == '':
        rows.append(cur.strip())
        cur = ''
        continue
    cur += ' ' + l
rows.append(cur.strip())

passports = []
for l in rows:
    p = {}
    for t in l.split():
        k, v = t.split(':')
        if 'cid' == k:
            continue
        p[k] = v
    passports.append(p)

def between(val, low, high):
    return low <= int(val) <= high

required_fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
valid_count = 0
for p in passports:
    if len(set(required_fields).intersection(p.keys())) != len(required_fields):
        continue

    if not (between(p['byr'], 1920, 2002) and between(p['iyr'], 2010, 2020) and between(p['eyr'], 2020, 2030)):
        continue

    h = p['hgt'][:-2]
    s = p['hgt'][-2:]
    if s not in 'cm' 'in':
        continue
    if s == 'cm' and not between(h, 150, 193):
        continue
    if s == 'in' and not between(h, 59, 76):
        continue

    if  p['ecl'] not in 'amb' 'blu' 'brn' 'gry' 'grn' 'hzl' 'oth':
        continue

    if not re.match(r'^\#[0-9a-f]{6}$', p['hcl']):
        continue

    if not re.match(r'^\d{9}$', p['pid']):
        continue

    valid_count += 1

print(valid_count)
