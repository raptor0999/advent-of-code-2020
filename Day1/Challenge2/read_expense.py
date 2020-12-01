expense_report = open("expensereport").readlines()
for lines in range(len(expense_report)):
	for morelines in range(len(expense_report)):
		for num, line in enumerate(expense_report, start=0):
			if((int(expense_report[lines]) + int(expense_report[morelines]) + int(expense_report[num])) == int(2020) and (lines != num) and (lines != morelines) and (num != morelines)):
				print("Numbers {} and {} and {}".format(expense_report[lines], expense_report[morelines], expense_report[num]))