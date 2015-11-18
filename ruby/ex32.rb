the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#first kind of array of FOR-LOOP through an array
for number in the_count
	puts "This is count #{number}"
end

#same as above bt usint a block
fruits .each do |fruit|
	puts "A fruit of type: #{fruit}"
end

#going through mixed arrays
for i in change
	puts "I got #{i}"
end
#we can build arrays startng with an empty on 
elements = []
#then use a range object to do 0..5 counts
for i in (0..5)
puts "Adding #{i} to the list."
#push a function that arrays undrstand
elements .push (i)
end

#now we can puts them too
for i in elements
	puts "Element was: #{i}"
	end
	
