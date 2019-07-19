import requests
import sys
import time

sys.path.insert(0, './script')
from get_links import *
from session import *
from comment import *
from inject import *
from BrokenAuthentification import *

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

    def startBroken(self):
        testlog = TestLog()
        dico = testlog.Launch()
        return dico


def main():
    scan = Scan()
    print("Cookie analyse ...")
    data = scan.startCookie()
    print('done')
    print('Comment bot analyse ...')
    Comment = scan.startComment()
    print('done')
    print('XSS injection analyse ...')
    xss = scan.startXSS()
    print('done')
    print('SQL Injection analyse ...')
    injection = scan.startInject()
    print('done')
    print('Broken Authentification analyse ...')
    broken = scan.startBroken()
    dictionnaries = []
    dictionnaries.append(data) 
    dictionnaries.append(Comment)
    dictionnaries.append(xss)
    dictionnaries.append(injection)
    dictionnaries.append(broken)
    return dictionnaries

print(main())