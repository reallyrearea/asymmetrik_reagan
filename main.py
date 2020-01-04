import re;

class Data:

	def __init__ (self):
		self.values = {}

	# determine if the word in in the list
	def word_exists (self, word, key):
		for val in range(0, len(self.values[key])):
			if self.values[key][val][1] == word:
				return val
		else:
			return None

	# get the value of the weight for sorting
	def get_key (self, item):
		return item[0]

	# add a data value to test data
	def add_val (self, word):
	
		word = word.lower()
		key = word[0:2]
		added = False
	
		if len(word) > 1:
			if key in self.values:
				
				# if the word is already in the list, val is the index
				# if the word does not exist, val is None
				val = self.word_exists(word, key)
				
				# if the word does not exist create a new value
				# for the word
				if val == None:
					self.values[key].append((0, word))
					self.values[key].sort(reverse = True, key = self.get_key)
				
				# if the word does exist, increment the weight
				else:
					weight = int(self.values[key][val][0])
					self.values[key][val] = (weight + 1, word)
					self.values[key].sort(reverse = True, key = self.get_key)
			# if there are no items in the list, create a new list
			else:
				self.values[key] = [(0, word)]

	# function to print stored values
	# for testing purposes
	def print_val (self):
	
		for i in self.values:
			print ("______________")
			print (i, ":")
			for j in self.values[i]:
				print (j)

	# get training data from a file
	def get_data (self, file):
		f = open (file, 'r')
		
		for line in f:
			for word in line.split():
				word =  re.sub('[^A-Za-z0-9]+', '', word)
				word = word.lower()
				self.add_val(word)
		
		f.close()

	# find word that matches user input best
	def find_word (self, word):
		
		word = word.lower()
		
		# if the index is in the dict
		if word[0:2] in self.values:
		
			n = len(word)
			# for each word in list
			for i in self.values[word[0:2]]:
				if i[1][0:n] == word:
					print ("Word:", i[1], "\t\tWeight:", i[0])
		
		else:
			print ("Could not find data for input.")

def main():
	data = Data()
	
	# can add training data from a file
	#data.get_data("file.txt")
	
	# can also add data by using add_val
	data.add_val("Asymmetrik")
	
	val = input("Enter: ")
	data.find_word(val)

main()