names = ['mike', 'brian', 'jones', 'clare', 'emmy']
email_domains = ['berg', 'cetten', 'gmail', 'google', 'borkan']

for i,j in zip(names, email_domains):
    email_address = i+"@"+j+".com"
    print email_address
