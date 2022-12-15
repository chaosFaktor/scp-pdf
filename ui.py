import os
import modules.banner as banner
import modules.ANSIcolour as ansi
import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import shared
import modules.scpDownloader as scpDownloader




def mainMenu():

    cui = [   ansi.RESET+'TstTitel' + 14*' '+ banner.lgbtq[0],
            'Bitte wähle eine der Optionen, um fortzufahren:' +6*' '+banner.lgbtq[1],
            ' '*53+banner.lgbtq[2],
            ]
        
    entr = ['Download as PDF'+' '*31+banner.lgbtq[5],
            'Download as HTML',
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
                scp=selUI.quitckInputPrompt('Bitte SCP-Nummer eingeben')
                scpDownloader.pdfDownload(scp)
            elif sel == entr[2]:
                pass

        os.system('clear')

