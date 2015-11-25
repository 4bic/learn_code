cities = {'KSM' => 'Kisumu', 
	'ELD' => 'Eldoret', 
	'NRB' => 'Nairobi'}

cities['NKS'] = 'Nakuru'
cities['MSA'] = 'Mombasa'

def find_city(map, state)
	if map.include? state
	return map[state]
	else
	return "Not found"		
	end
end

cities[:find] = method(:find_city)

while true
print "State? (ENTER to quit) "
state = gets.chomp

break if state.empty?
puts cities[:find]. call(cities, state)	
end
