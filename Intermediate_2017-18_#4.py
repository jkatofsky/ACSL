letters, counts, histories = [], [], []

def add (chars):
	global letters, counts, histories
	for char in chars:
		if char.isalpha():
			if char in letters:
				counts[letters.index(char)] += 1
			else:
				tempLetters = letters[:]
				tempLetters.append(char)
				letters = sorted(tempLetters)
				counts.insert(letters.index(char), 1)
				histories.append("")
				for i in range(letters.index(char), len(letters)):
					histories[i] += letters[i]

def delete (chars):
	global letters, counts, histories
	for char in chars:
		if char.isalpha():
			if char in letters:
				index = letters.index(char)
				if counts[index] is 1:
					del counts[index]
					del letters[index]
					for i in range(index, len(letters)):
						histories[i] += letters[i]
				else:
					counts[index] -= 1

def reset (chars):
	global letters, counts, histories
	letters, counts, histories = [], [], []
	add(chars)

def report (index):
	print(histories[int(index)-1])

inputToCommand = {"ADD" : add, "DELETE": delete, "RESET": reset, "REPORT": report}
while True:
	userInput = input("Enter a command: ").upper().split(" ", 1)
	inputToCommand[userInput[0]](userInput[1])
