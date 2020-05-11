import time
from datetime import datetime as dt

hostpath = r"C:\Windows\System32\drivers\etc\hosts"
hosttemp = r"C:\Users\USER\Desktop\python\build apps\3. website blocker\hosts"
# r tells python the string is a row string
# where the hosts file is stored

website_list = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]
# list of websites I want to block

redirect = '127.0.0.1'
# redirect attempts to load those websites to this IP address

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours!")

        # open and modify the hosts file now
        with open(hostpath, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        # we need to open the hosts file and delete the newly added
        # websites if they are currently in the file
        with open(hostpath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            # returns the cursor to the start of the content
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            # removes all lines after the original lines
            # have been written
            
        print("Nonworking hours...")
    time.sleep(5)   