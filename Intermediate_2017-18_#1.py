cardFaceValues = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}

def cardToPoints(card, points):
	if card == "9":
		return 0
	elif card == "T":
		return -10
	elif card == "A" and (points + 14) > 99:
		return 1
	return cardFaceValues[card]

def playACSL99(initialPoints, initialPlayerCards, playerCardsToPickUp, dealerCardsToPlay):
	totalPoints, playerCards = initialPoints, initialPlayerCards
	while (totalPoints <= 99):
		largest = playerCards[0]
		for card in playerCards[1:]:
			if cardFaceValues[card] > cardFaceValues[largest]:
				largest = card
		totalPoints += cardToPoints(playerCards.pop(playerCards.index(largest)), totalPoints)
		playerCards.append(playerCardsToPickUp.pop(0))
		if totalPoints > 99:
			print(str(totalPoints) + ", dealer")
			break
		totalPoints += cardToPoints(dealerCardsToPlay.pop(0), totalPoints)
	else:
		print(str(totalPoints) + ", player")

if __name__ == '__main__':
	inputs = []
	for i in range (5):
		inputs.append(input("Enter the one-character strings seperated by commas (whitespace and capitalization doesn't matter): ")
		.upper().replace(" ","").split(","))
	for ish in inputs:
		playACSL99(initialPoints = int(ish[0]), initialPlayerCards = [card for card in ish[1:4]],
		playerCardsToPickUp = [card for card in ish[4::2]], dealerCardsToPlay = [card for card in ish[5::2]])
