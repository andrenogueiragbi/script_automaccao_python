
banner = '''
                                                               EE
                                                              EE
      A        NNN        NN  DDDDDD       RRRRRRRRR     EEEEEEEEEE
     AAA       NNNN       NN  DDDDDDDDD    RR      RRR   EE
    AA AA      NN NNN     NN  DD      DDD  RR      RRR   EE
   AA   AA     NN   NN    NN  DD       DD  RRRRRRRRR     EEEEEEE
  AAAAAAAAA    NN     NNN NN  DD      DDD  RR     RRR    EE
 AA       AA   NN       NNNN  DDDDDDDDD    RR      RRR   EE
AA         AA  NN        NNN  DDDDDD       RR       RRR  EEEEEEEEEE

André Pereira Nogueira V 0.0  (C)    2020-2021     http://www.andretec.com.br/
'''

print(banner)


import pyautogui as comando
import time as tempo



def abraAbaNew():
    comando.hotkey('ctrl','t')

comando.PAUSE = 0.7

#Abrindo o windows
comando.hotkey('winleft')

#Abrindo o chrome
comando.write('Google Chrome')
comando.hotkey('down')
comando.hotkey('enter')

#Abrindo o whatasapp
zap = 'https://web.whatsapp.com/'
comando.write(zap)
comando.hotkey('enter')

#abrindo utra aba
abraAbaNew()

#Abrindo o whatasapp
mail = 'site.com.br'
comando.write(mail)
comando.hotkey('enter')
comando.hotkey('enter')

#abrindo utra aba
abraAbaNew()
''
#Abrindo o whatasapp
grafana = 'site.com.br'
comando.write(grafana)
comando.hotkey('enter')

#abrindo utra aba
abraAbaNew()

#Abrindo o whatasapp
link = 'site.com.br'
comando.write(link)
comando.hotkey('enter')
comando.hotkey('tab')
comando.write('USER')
comando.hotkey('tab')
comando.write('SENHA')
comando.hotkey('enter')








