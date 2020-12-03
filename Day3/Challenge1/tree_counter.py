tree_map = open("tree_input").read().splitlines()
currentX = 0
currentY = 0
stepX = 3
stepY = 1
tree_count = 0
hack_step = False

#y bounds are naturally contained by for in since Y step is 1
for num, line in enumerate(tree_map, start=0):
	# if modulus only for y step 2
	#if(num%2 == 0):
	print("Char at {}, {}: {}".format(str(currentX), str(currentY), line[currentX]))
	if(line[currentX] == "#"):
		tree_count += 1

	# test x bounds before increment
	if(len(line) > currentX+stepX):
		currentX += stepX
		currentY += stepY
	else:
		for i in range(1, stepX+1):
			# test for reset condition
			if(len(line) == currentX+1 or line[currentX] == ""):
				currentX = -1
				currentY += 1

			currentX+=1
print("Total tree count: {}".format(str(tree_count)))