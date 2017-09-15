import time
from datetime import datetime as dt

# determine where the host file is located
hosts_temp = 'hosts'
hosts_path =  "/etc/hosts"
# prefered url to redirect from distracting sites
redirect = "127.0.0.1"
# sites to be blocked from
website_list = ["www.facebook.com", "www.twitter.com", "mail.google.com"]

while True:
    # check what time it is
    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working hours ....")
        # open the hosts file
        with open(hosts_path, 'r+') as file:
            # save details in a variable
            content = file.read()
            # check presence of our domains to be evaluated
            for website in website_list:
                # if domain exist move on
                if website in content:
                    pass
                else:
                    # otherwise add it(domain name) to list of redirects
                    file.write(redirect+" "+ website+"\n")

    else:
        # open the hostfile again
        with open(hosts_path, 'r+') as file:
            # store details in a form we can pass around
            content = file.readlines()
            # move pointer to top of file
            file.seek(0)
            for line in content:
                # check presence of domains in list otherwise write it
                if not any(website in line for website in website_list):
                    file.write(line)
            # removes all details at the bottom of file to prevent duplication
            file.truncate()
        print ("Fun hour . . . .")
    time.sleep(5)
