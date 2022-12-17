import os
import modules.ANSIcolour as ansi
escapeMessage=[ansi.BOLD+'---End of Programm---'+ansi.RESET]
def escape():
    for i in escapeMessage:
        print(i)
    while True:
        quit()

cwd=os.getcwd()
cssdir=__file__.rsplit('/', 1)[0]+'/css/'
cssdefaultdir=__file__.rsplit('/', 1)[0]+'/default.css'
maindir=__file__.rsplit('/', 1)[0]