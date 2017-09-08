def ksh_to_dollars(rate, shillings):
    dollars = shillings / rate
    return dollars

r = float(input("Enter the exchange rate : "))
sh = float(input("How much shillings would you like to convert?  : "))

print 'That is equivalent to',ksh_to_dollars(r,sh), 'dollars'
