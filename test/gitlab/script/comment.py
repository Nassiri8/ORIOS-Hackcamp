import requests
import time
from progessbar import printProgressBar

class Comment:
    def postToComment(self, targetURL):
        #Data passer dans le post
        data = {
            'pseudo':"DEAMON",
            'status':'1',
            'message':"Je suis le bot du diable #DEAMON #1"
        }

        i = 0
        while i < 10:
            printProgressBar(i, 9, prefix = 'Progress:', suffix = 'Complete', length = 35)
            result = requests.post(targetURL, data)
            time.sleep(1)
            i += 1
        return result

    #Script pour remplir l'espace commentaire
    def comments(self, targetURL):
            self.postToComment(targetURL)
            return True 

    #Msg send for le pdf
    def msgToPdfBot(self, targetURL):
        if self.comments(targetURL) == True:
            return "Votre WebSite n'est pas protégé contre les bot sur la partie commentaire"

    def xssInjection(self, targetUrl):
        data = {
            'pseudo':"DEAMON",
            'status':'1',
            'message':"<script>alert('Terrence recupère Sarah c la femme de ta life')</script>"
        }
        result = requests.post(targetUrl, data)
        if result.status_code == 200:
            return "XSS Injection done d'une balise script"
        return "No Xss Injection GG"