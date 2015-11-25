ten_things = "Apples Oranges Crows Telephone Light Sugar"
puts "the ten items are: #{ten_things}"

puts "Wait there's not 10 things in that list let's fix that."
stuff = ten_things.split(' ')
more_stuff = %w(Day Night Song Frisbee Banana Girl Boy)

while stuff.length != 10
	next_one = more_stuff.pop()
	puts "Adding: #{next_one}"
	stuff.push(next_one)
	puts "There's #{stuff.length} items now."
end

puts "There we go #{stuff}"

puts "Lets do some things with stuff."

puts stuff[1]
puts stuff.pop()
puts stuff.join(' ')# what? cool!
puts stuff.values_at(3,5).join('#') #super stellar