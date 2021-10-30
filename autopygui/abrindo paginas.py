
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

# sudo apt-get install python3-tk
import time as tempo 
import pandas as pd
import pyperclip as clique
comando.alert("TIRA A MÃO, QUE AGORA É COMIGO, RSRSRSRSRS")



comando.PAUSE = 1
link = 'www.teste.com.br' 
#pyautogui.hotkey('win')

comando.click(20,20)
comando.write('Google Chrome')
comando.click(263,62)


comando.write(link)
comando.hotkey('enter')




comando.click(662,458)
comando.write('USER')


comando.hotkey('tab')



comando.write('SENHA')
comando.hotkey('tab')
comando.hotkey('enter')


comando.click(93,151)

comando.click(344,205)




comando.click(265,245)
comando.write('FULANO DE TAL')
comando.hotkey('enter')



comando.click(620,375,clicks=2)

comando.click(162,457)



comando.click(872,197)

comando.click(1211,703)



comando.click(508,475)

comando.hotkey('down')
comando.hotkey('enter')


comando.click(1196,707)

comando.click(579,227)
comando.hotkey('down')
comando.hotkey('enter')


comando.click(453,366)


problema = '''
Cliente ligou com lentidão, todavia não quis fazer os teste, sinal da ONU 25.3,
O cliente disse que não pode atender a noite
levar roteador a noite

'''
comando.write(problema)
#botão avançar
comando.click(1207,708)
#abaixo scrol para baixo
comando.click(1339,333)
#escolhe tipo de atendimento
comando.click(415,293)

comando.click(1339,333,clicks=3)

comando.click(465,309)

comando.click(1339,333)
comando.click(492,293)
#destino para o atendimento
comando.click(408,393)

comando.write('FULANO DE TAL')
comando.hotkey('down')

comando.hotkey('enter')

comando.click(460,472)

comando.write(problema)

comando.hotkey('tab')
comando.hotkey('down')
comando.hotkey('tab')

for i in range(3):
    comando.hotkey('down')
for i in range(5):
    comando.hotkey('tab')
for i in range(2):
    comando.hotkey('enter')


comando.alert("OS GERADA COM SUCESSO!!!")


