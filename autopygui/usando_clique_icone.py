
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
comando.PAUSE = 2

url = 'https://app.feedz.com.br/inicio'



#abrindo navegador
comando.click('/home/user/github/projetos_python/automacao/image_feedz/chome.png',clicks=2)

#digitando url
comando.write(url)
comando.hotkey('enter')


comando.click(942,505)
comando.move(0,120)

comando.click()

mensagem = 'Deus é bom'

comando.write(mensagem)

comando.click('/home/user/github/projetos_python/automacao/image_feedz/enviar.png')



