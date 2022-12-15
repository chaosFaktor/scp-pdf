import os
import modules.banner as banner
import modules.ANSIcolour as ansi
import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import shared
import scpDownloader as scpDownloader




def mainMenu():
    os.system('clear')

    cui = [   ansi.RESET+'Input credentials accepted' + 14*' '+ banner.lgbtq[0],
            'Welcome to the SCP-Database, operator' +8*' '+banner.lgbtq[1],
            ' '*53+banner.lgbtq[2],
            ]
        
    entr = ['Download SCP'+' '*31+banner.lgbtq[5],
            'Download universal',
            'Exit']
            
            
    curSelui=selUI.SelectionMenu.create(entr, '<t>')

    while True:
        for i in cui:
            print(i)
        print(curSelui.refresh().replace('<t>', ' '*53+banner.lgbtq[3]).replace('▄'*100, '▄'*30+' '*23+banner.lgbtq[4]))
            
        try:
            inp = uniKey.getch()
        except InterruptedError:
            shared.escape()
        if inp in 'wW8':
            curSelui.selDown()
        elif inp in 'sS2':
            curSelui.selUp()
        elif inp in 'dD6 \n':
            os.system('clear')
            # Elif since switch statements suck in python
            sel=curSelui.select()
            if sel == entr[0]:
                scp=scpDownloader.scpPrompt()
                css=scpDownloader.cssPrompt()
                scpDownloader.pdfDownload(scp, css)
            elif sel == entr[2]:
                scp=scpDownloader.uniPrompt()
                css=scpDownloader.cssPrompt()
                scpDownloader.pdfDownload(scp, css)

        os.system('clear')

