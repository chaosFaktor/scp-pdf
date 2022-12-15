import os
import requests
from bs4 import BeautifulSoup
import shared
import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import modules.ANSIcolour as ansi

def convertHtmlToPdf(soup, out='./out'):
    import pdfkit
    pdfkit.from_file('./out.html', out+'.pdf', options={"enable-local-file-access": True})
    
def scpPrompt():
    inp =''
    while inp=='':
        os.system('clear')
        print('Please enter the scp-identification number below')
        inp=input('SCP-')
    return inp
def cssPrompt():
    os.system('clear')
    files = os.listdir(shared.cssdir)
    menu = selUI.SelectionMenu.create(files, 'Please select your prefered theme', selUI.SelectionMenu.defaultOptions)
    while True:

        print(menu.refresh())
        inp=uniKey.getch()
        os.system('clear')
        if inp in 'wW8':
            menu.selDown()
        elif inp in 'sS2':
            menu.selUp()
        elif inp in 'dD56 \n':
            return shared.cssdir+menu.select()
        

def dwnld_raw_scp(scp):
   url='https://scp-wiki.wikidot.com/scp-'+str(scp)
   site=requests.get(url)
   soup=BeautifulSoup(site.text, features='lxml')
   scptxt=soup.find('div', {'id': 'page-content'})
   scptxt.find('div', {'class': 'collapsible-block-unfolded'})['class'] = ''
   return scptxt

def loadCSS(soup, css):
    try:
        default_css = open(shared.cssdefaultdir, 'r').read()
        new_css = open(css, 'r').read()
        soup.append(BeautifulSoup(new_css, features='lxml'))
        soup.append(BeautifulSoup(default_css, features='lxml'))
        return soup
    except:
        print(ansi.Bold.RED+'ERROR! Konnte CSS '+css+' nich laden' +ansi.RESET)
        raise NameError


def pdfDownload(scp, css, out=''):
    html=dwnld_raw_scp(scp)
    html=loadCSS(html, css)
    open('./out.html', 'w').write(html.prettify())
    convertHtmlToPdf(html)
    shared.escape()


