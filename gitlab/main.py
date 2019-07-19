import requests
import sys
import time

sys.path.insert(0, './script')
from get_links import *
from session import *
from comment import *
from inject import *

class Scan:
    def startCookie(self):
        Getlinks = Get_Link()
        session = Session()
        link = Getlinks.launch()
        i = 0 
        url = []
        tokens = []
        dictionnary = {
            'PHPSESSID': {
                'data': {
                    'url': url,
                    'tokens': tokens,
                    'msg': 'Récupère le token de session',
                }
            } 
        }
        while i < len(link):
            if session.cookiePHP(link[i]) is not None:
                print(link[i])
                url.append(link[i])
                token = session.cookiePHP(link[i])
                tokens.append(token)
            i = i + 1
        return dictionnary

    def startComment(self):
        Getlinks = Get_Link()
        session = Session()
        links = Getlinks.launch()
        comment = Comment()
        i = 0
        url = []

        dictionnary = {
            'Boot SPAM BDD': {
                'data': {
                    'url': url,
                    'msg': 'Le site est vulnérable à la faille A7 Cross-Site Scripting (XSS) dans les commentaires',
                }
            } 
        }
        while i < len(links):
            if links[i] == "http://orios.louisviallon.fr/commentaires.php":
                comment.msgToPdfBot(links[i])
                url.append(links[i])
            i += 1
        return dictionnary

    def startXSS(self):
        Getlinks = Get_Link()
        session = Session()
        links = Getlinks.launch()
        comment = Comment()
        i = 0
        url = []

        dictionnary = {
            'XSS': {
                'data': {
                    'url': url,
                    'msg': 'Le site est vulnérable à la faille A7 Cross-Site Scripting (XSS)',
                }
            } 
        }
        while i < len(links):
            if links[i] == "http://orios.louisviallon.fr/commentaires.php":
                msg = comment.xssInjection(links[i])
                url.append(links[i])
            i += 1
        return dictionnary

    def startInject(self):
        Getlinks = Get_Link()
        inject = Inject()
        link = Getlinks.launch()
        i = 0 
        url = []

        dictionnary = {
            'Injection SQL': {
                'data': {
                    'url': url,
                    'msg': 'Le site est vulnérable à la faille injection SQL dans la partie login (marcel" OR 1=1#)',
                }
            } 
        }
        while i < len(link):
            if inject.injectop(link[i]) is True:
                url.append(link[i])
            i += 1
        return dictionnary


def main():
    scan = Scan()
    data = scan.startCookie()
    data1 = scan.startComment()
    data2 = scan.startXSS()
    data3 = scan.startInject()
    array = []
    array.append(data) 
    array.append(data1)
    array.append(data2)
    array.append(data3)
    return array