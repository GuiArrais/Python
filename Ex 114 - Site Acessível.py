#Crie um código em Python que teste se o site Pudim está acessível 
#pelo computador usado.
import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com')
except urllib.error.URLError:
    print('\033[31mO site não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site com sucesso.\033[m')
    # print(site.read())