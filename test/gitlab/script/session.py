import requests

class Session:
    #Get le PHPSESSID des cookie
    def cookiePHP(self, target):
        result = requests.get(target)
        json= result.headers
        try: 
            id = json['Set-Cookie']
            phpid = id.split(';')
            session = phpid[0].split('=')
            return session[1] 
        except:  
            return None