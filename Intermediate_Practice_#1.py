import sys

def numToBaseStr(num,base):
	if num < base:
		return str(num)
	return numToBaseStr(num//base,base) + str(num%base)

def addReversed(num, base):
	convertedNum = int(str(num), base)
	reversedConvertedNum = int(str(num)[::-1], base)
	return numToBaseStr(convertedNum + reversedConvertedNum, base)

def isPalindrome(n):
	return str(n) == str(n)[::-1]

if __name__ == "__main__":
	num, base = int(sys.argv[1]), int(sys.argv[2])
	repetitions = 0
	while not isPalindrome(num):
		repetitions+=1
		if repetitions is 11:
			break
		num = addReversed(num, base)
	else:
		print(str(num))
		sys.exit()
	print ("NONE, " + str(num))
	sys.exit()
