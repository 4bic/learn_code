import time
from datetime import datetime as dt

# determine where the host file is located
hosts_path = "/etc/hosts"
# prefered url to redirect from distracting sites
redirect = "127.0.0.1"
# sites to be blocked from
website_list = ["www.facebook.com", "www.twitter.com", "mail.google.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours ....")
    else:
        print ("Fun hour . .('_')")
    time.sleep(5)
