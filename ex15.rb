=begin
#declares the file specified as an argument and thus will be 
#used in the entire file
filename = ARGV.first
#provides allocation for user to enter an obect name 
prompt = ">"
#opens up the file
txt File.open(filename)
#outputs the values under the double quotes with a call back of the argumented file
puts "Here's your file: #{filename}"
#reads the file without parameters
puts txt.read()
 
 puts "I'll ask you to type it again:"
 print prompt
 file_again = STDIN.gets.chomp()

 txt_again = File.open(file_again)

 puts txt_again.read()
=end
#outputs the value under the double quotes
puts "What file do you want to open? :"
#provides an input field
prompt = ">"
# makes the declared input, an argument
filename = STDIN.gets.chomp()
#the input object is manipulated
txt = File.open(filename)
#Outputs the value under the double quotes with a callback of the argumented object
puts "Here's your file: #{filename}"
puts txt.read()
puts txt.close()