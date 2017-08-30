negation_words = ['not', 'no']
positive_words = ['good', 'nice'] 
your_string = "This is not good"
list_of_words = your_string.split()
for neg_word in negation_words:
	if neg_word in list_of_words:
		next_word = list_of_words[list_of_words.index(neg_word) + 1]
		print(next_word)
		print("negatif")