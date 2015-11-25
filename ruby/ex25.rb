module Ex25
	def self.break_words(stuff)
		#this function breaks down words
		words = stuff.split(' ')
		words
	end

	def self.sort_words(words)
		#sorts the words
		words.sort()
	end

	def self.print_first_word(words)
	# Prints the first word and shifts the others down by one.
		word = words.shift()
		puts word
	end

	def self.print_last_word(words)
		#prints last word after popping it off the end
		word = words.pop()
		puts word
	end

	def self.sort_sentence(sentence)
		#Takes in full sentence and returns the sorted words.
		words = break_words(sentence)
		sort_words(words)		
	end

	def self.print_first_and_last(sentence)
		#prints first and last words of the sentence
		words = break_words(sentence)
		print_first_word(words)
		print_last_word(words)
	end

	def self.print_first_and_last_sorted(sentence)
		#sorts the words the prints the first and last one.
		words = sort_sentence(sentence)
		print_first_word(words)
		print_last_word(words)
	end
end







