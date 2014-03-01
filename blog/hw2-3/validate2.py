import pymongo
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import random
import re
import string

# makes a little salt
def make_salt(n):
    salt = ""
    for i in range(n):
        salt = salt + random.choice(string.ascii_letters)
    return salt


# this is a validation program to make sure that the blog works correctly.

def create_user(username, password):
    try:
        print("Trying to create a test user ", username)
        cj = http.cookiejar.CookieJar()
        url = "http://localhost:8082/signup"

        data = urllib.parse.urlencode([("email",""),("username",username), ("password",password), ("verify",password)])
        encoded_data = data.encode('ascii')
        request = urllib.request.Request(url=url, data=encoded_data)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        f = opener.open(request)

        # check that the user is in the user table
        connection = pymongo.Connection("mongodb://localhost", safe=True)
        db = connection.blog
        users = db.users
        user = users.find_one({'_id':username})
        if (user == None):
            print("Could not find the test user ", username, "in the users collection.")
            return False
        print("Found the test user ", username, " in the users collection")

        # check that the user has been built
        result = f.read().decode('ascii')
        expr = re.compile("Welcome\s+"+ username)
        if expr.search(result):
            return True
        
        print("When we tried to create a user, here is the output we got\n")
        print(result)
        
        return False
    except Exception as e:
        print("the request to ", url, " failed, so your blog may not be running.")
        print("EXCEPTION: create_user: " + str(e))
        return False


def try_to_login(username, password):

    try:
        print("Trying to login for test user ", username)
        cj = http.cookiejar.CookieJar()
        url = "http://localhost:8082/login"

        data = urllib.parse.urlencode([("username",username), ("password",password)])
        encoded_data = data.encode('ascii')
        request = urllib.request.Request(url=url, data=encoded_data)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        f = opener.open(request)

        # check for successful login
        result = f.read().decode('ascii')
        expr = re.compile("Welcome\s+"+ username)
        if expr.search(result):
            return True

        print("When we tried to login, here is the output we got\n")
        print(result)
        return False
    except Exception as e:
        print("the request to ", url, " failed, so your blog may not be running.")
        print("EXCEPTION: try_to_login:" + str(e))
        raise
        return False


username = make_salt(7)
password = make_salt(8)

# try to create user

if (create_user(username, password)):
    print("User creation successful. ")
    # try to login
    if (try_to_login(username, password)):
        print("User login successful.")
        print("Validation Code is ", "h726dgdf63289wjaklf9467ghdsjkf")
    else:
        print("User login failed")
        print("Sorry, you have not solved it yet.")

else:
    print("Sorry, you have not solved it yet.")

