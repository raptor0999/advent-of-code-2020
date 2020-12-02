pw_db = open("pw_db").readlines()
valid_pw_count = 0

for line in pw_db:
	policy_and_pw = line.split(": ")
	letter_amount_range_and_letter = policy_and_pw[0].split(" ")
	low_and_high_range = letter_amount_range_and_letter[0].split("-")
	letter_needed = letter_amount_range_and_letter[1]
	low_position = int(low_and_high_range[0])
	high_position = int(low_and_high_range[1])
	password = policy_and_pw[1]
	is_letter_in_low_position = False
	is_letter_in_high_position = False

	if(password[low_position-1] == letter_needed):
		is_letter_in_low_position = True

	if(password[high_position-1] == letter_needed):
		is_letter_in_high_position = True

	if((is_letter_in_low_position and not is_letter_in_high_position) or (not is_letter_in_low_position and is_letter_in_high_position)):
		print("Policy: Letter {} needed in position {} and position {}".format(letter_needed, low_position, high_position))
		print("Password: " + password)
		
		print("")
		valid_pw_count += 1

print("Valid password count: " + str(valid_pw_count))