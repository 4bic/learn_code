import time
from datetime import datetime as dt

# determine where the host file is located
hosts_temp = 'hosts'
#hosts_path =  "/etc/hosts"
# prefered url to redirect from distracting sites
redirect = "127.0.0.1"
# sites to be blocked from
website_list = ["www.facebook.com", "www.twitter.com", "mail.google.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours ....")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")

    else:
        print ("Fun hour . .('_')")
    time.sleep(5)
