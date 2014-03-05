## r/dailyprogrammer | Challenge 149 | Disemvowler

vowellist = list("aeiou")
inp = raw_input("Enter text here: ")
listofwords = inp.split()

def disemvowel(words):

	conword = ""
	vowword = ""
	
	for idx, word in enumerate(words):
		tempword = word
		letters = list(word)
		for letter in letters:
			for v in vowellist:
				if v in letter:
					vowword += letter
					letters.remove(v)
					w = ''.join(letters)
					conword += w
		
	return conword, vowword					

cw, vw = disemvowel(listofwords)
print("New string: " + cw + "\n")
print("The vowels: " + vw)