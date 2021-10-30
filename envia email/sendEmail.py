import smtplib
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'teste@gmail.com'
password = 'passwdOfemail'

from_addr = 'teste@gmail.com'

email = [
    'destino@gmail.com',
    'destino1@gmail.com',
    'destino2@gmail.com',
    'destino3@gmail.com',
    'destino4@gmail.com',
]

for a in email:
    print(a)


    mensagem = '''
Wello World!!!!!!!!!
    '''
    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    message = MIMEText(mensagem)
    message['subject'] = ' TITULO DO EMAIL'
    message['from'] = from_addr
    message['to'] = ', '.join(a)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, a, message.as_string())
    server.quit()

