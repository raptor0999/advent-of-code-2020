pw_db = open("pw_db").readlines()
valid_pw_count = 0

for line in pw_db:
	policy_and_pw = line.split(": ")
	letter_amount_range_and_letter = policy_and_pw[0].split(" ")
	low_and_high_range = letter_amount_range_and_letter[0].split("-")
	letter_needed = letter_amount_range_and_letter[1]
	low_range = int(low_and_high_range[0])
	high_range = int(low_and_high_range[1])
	password = policy_and_pw[1]
	letter_count = password.count(letter_needed)
	within_min_range = letter_count >= low_range
	within_max_range = letter_count <= high_range

	if(within_min_range and within_max_range):
		print("Policy: Letter needed is {} and min occurences is {} and max occurences is {}".format(letter_needed, low_range, high_range))
		print("Password: " + password)
		print("Letter count in password: {}".format(letter_count))
		print("Within min range? {}".format(within_min_range))
		print("Within max range? {}".format(within_max_range))
		print("")
		valid_pw_count += 1

print("Valid password count: " + str(valid_pw_count))