import re
import ast

passport_entries = open("passport_input", "rb").readlines()
passport_number = 0
passports = []
passport = {}

for num, line in enumerate(passport_entries, start=0):
	if(line != b'\r\n'):
		for item in line.split(b" "):
			key_val_pair = item.split(b":")
			passport[key_val_pair[0]] = key_val_pair[1]
	else:
		passports.append(passport)
		passport_number += 1
		passport = {}

valid_passports = 0
for p in passports:
	if(b'hgt' in p):
		height_val = p[b'hgt'].decode('utf-8')
		height_num = int(''.join(list(filter(str.isdigit, height_val))))
	else:
		height_num = 0

	if((b'byr' in p and int(p[b'byr']) >= 1920 and int(p[b'byr']) <= 2002)) and (b'iyr' in p and int(p[b'iyr']) >= 2010 and int(p[b'iyr']) <= 2020) and (b'eyr' in p and int(p[b'eyr']) >= 2020 and int(p[b'eyr']) <= 2030) and (b'hgt' in p and ((b'cm' in p[b'hgt'] and height_num >= 150 and height_num <= 193) or (b'in' in p[b'hgt'] and height_num >= 59 and height_num <= 76))) and (b'hcl' in p and (re.match(b'#[0-9a-f]{6}', p[b'hcl']))) and (b'ecl' in p and (p[b'ecl'] == b'amb' or p[b'ecl'] == b'blu' or p[b'ecl'] == b'brn' or p[b'ecl'] == b'gry' or p[b'ecl'] == b'grn' or p[b'ecl'] == b'hzl' or p[b'ecl'] == b'oth')) and (b'pid' in p and p[b'pid'].decode('utf-8').isdigit() and len(p[b'pid'].decode('utf-8')) == 9):
		valid_passports += 1
		print(p)
		print("Birth year: " + str(int(p[b'byr'])))
		print("Issue year: " + str(int(p[b'iyr'])))
		print("Expire year: " + str(int(p[b'eyr'])))
		print("Height: " + p[b'hgt'].decode('utf-8'))
		print("Hair color: " + p[b'hcl'].decode('utf-8'))
		print("Eye color: " + p[b'ecl'].decode('utf-8'))
		print("Passport ID: " + p[b'pid'].decode('utf-8'))

print("Size of passports: " + str(len(passports)))
print("Num of passports: " + str(passport_number))
print("Valid passports: " + str(valid_passports))