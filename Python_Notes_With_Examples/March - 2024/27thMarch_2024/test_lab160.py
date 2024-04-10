#Env file (.dot env file)
#Hiw do yoi store the password or credentials in the framework
#pip install python-dotenv

from dotenv import load_dotenv
import os

"""def test_login():
    username = "Admin"
    password = "password"
    assert username == "Admin"
    assert password == "password"
    #this is not a best practice so we create a new file"""

def test_login():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)