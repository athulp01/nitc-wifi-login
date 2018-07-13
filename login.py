#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup 
import re

sess = requests.Session()
response = sess.get("http://clients3.google.com/generate_204")
if response.status_code is not 204:
    page = response.text
    soup = BeautifulSoup(page,'html5lib')
    attr = {"name":"magic", "type":"hidden"}
    c= soup.find('input',attrs=attr)

    magic = c['value']
    username = "yourrollnumber"
    password = "yourpassword"
    redir = "http://clients3.google.com/generate_204"

    post_data = {"username":username, "password":password, "magic":magic,"4Tredir":redir}
    print(magic)
    url = "http://172.16.12.1:1000/fgtauth?"
    res = sess.post(url+magic,data=post_data)
    logout_code = res.url.split('?')[1]
    print("Log out url is http://172.16.12.1:1000/logout?"+logout_code)
    file = open("/home/athul/logout.code","w+")
    file.write(logout_code)  
else:
    print("You are already authenicated!")

