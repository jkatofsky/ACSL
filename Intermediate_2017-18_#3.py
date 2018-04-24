def getGrid(hexArray):
	grid = [[None for c in range(8)] for r in range (8)]
	for r in range (len(hexArray)):
		binaryNumber = bin(int(hexArray[r], 16))[2:].zfill(8)
		for c in range (len(binaryNumber)):
			grid[r][c] = int(binaryNumber[c])
	return grid

leftAngleToDirection = { 90: "B", 180: "L", 270: "A", 360: "R" }
rightAngleToDirection = { 90: "A", 180: "R", 270: "B", 360: "L" }
belowAngleToDirection = { 90: "R", 180: "B", 270: "L", 360: "A" }
aboveAngleToDirection = { 90: "L", 180: "A", 270: "R", 360: "B" }

def getNextDirection (currDirection, angle):
	if currDirection == "L":
		return leftAngleToDirection[angle]
	elif currDirection == "R":
		return rightAngleToDirection[angle]
	elif currDirection == "B":
		return belowAngleToDirection[angle]
	elif currDirection == "A":
		return aboveAngleToDirection[angle]

leftAngleToMovement = { 90: [-1, 0], 180: [0, 1], 270: [1, 0], 360: [0, -1] }
rightAngleToMovement = { 90: [1, 0], 180: [0, -1], 270: [-1, 0], 360: [0, 1] }
belowAngleToMovement = { 90: [0, -1], 180: [-1, 0], 270: [0, 1], 360: [1, 0] }
aboveAngleToMovement = { 90: [0, 1], 180: [1, 0], 270: [0, -1], 360: [-1, 0] }

def getNextLocation(walkerLoc, direction, angle):
	if direction == "L":
		walkerLoc = [i + j for i, j in zip(walkerLoc, leftAngleToMovement[angle])]
	elif direction == "R":
		walkerLoc = [i + j for i, j in zip(walkerLoc, rightAngleToMovement[angle])]
	elif direction == "B":
		walkerLoc = [i + j for i, j in zip(walkerLoc, belowAngleToMovement[angle])]
	elif direction == "A":
		walkerLoc = [i + j for i, j in zip(walkerLoc, aboveAngleToMovement[angle])]
	for i in range(len(walkerLoc)):
		if walkerLoc[i] is -1:
			walkerLoc[i] = 7
		if walkerLoc[i] is 8:
			walkerLoc[i] = 0
	return walkerLoc

def getAngle (turnValue):
	if turnValue is 0:
		return 180
	angle = 0
	for i in range (turnValue):
		angle += 90
	if angle > 360:
		angle = angle % 360
	return angle

def getFinalLocation(grid, walkerLoc, direction, numMoves):
	turnValues = [[column for column in row] for row in grid]
	for i in range(numMoves):
		angle = getAngle(turnValues[walkerLoc[0]][walkerLoc[1]])
		if turnValues[walkerLoc[0]][walkerLoc[1]] is not 0:
			turnValues[walkerLoc[0]][walkerLoc[1]] += 1
		walkerLoc = getNextLocation(walkerLoc, direction, angle)
		direction = getNextDirection(direction, angle)
	return [walkerLoc[0], walkerLoc[1]]

grid = getGrid(input("Input hexadecimal values for the 2D array (seperated by commas): ").replace(" ","").split(","))
inputs = []
for i in range(5):
	inputs.append(input("Input instructions for the #%i walker (seperated by commas): " % (i+1)).replace(" ","").split(","))
for walkerInstructions in inputs:
	finalLocation = getFinalLocation(grid, walkerLoc = [int(coord)-1 for coord in walkerInstructions[:2]], direction = walkerInstructions[2], numMoves = int(walkerInstructions[3]))
	print("Final location of the #%i walker (row, column): %s, %s" % (inputs.index(walkerInstructions)+1, str(finalLocation[0]+1), str(finalLocation[1] + 1) ) )
