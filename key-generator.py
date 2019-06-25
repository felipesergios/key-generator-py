from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string
import time
import mysql.connector
from mysql.connector import errorcode

# create message object instance
msg = MIMEMultipart()
#Gerador
letras = string.ascii_letters

codigo1 = ''.join(random.choice(letras) for _ in range(4))
codigo5 = ''.join(random.choice(letras) for _ in range(9))
codigo2=random.randint(0,10)
codigo3=random.uniform(1.5, 5.75)
codigo4=random.randint(0,10)
B=('{}-{}-{:.2f}-{}{}'.format(codigo1,codigo2,codigo3,hex(codigo4)[2:],codigo5))
print(B)
#continua-------------------
try:
    cnx = mysql.connector.connect(user='python', password='123', host='127.0.0.1', database='PYTHON3',
                                  use_pure=False)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    mycursor = cnx.cursor()
    sql = "INSERT INTO senhas (pass_wd, data_passwd) VALUES (%s, %s)"
    A = str(input('Valor Para Senha:'))
    #B = str(input('Endereço:'))
    val = (A, B)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record inserted.")
#----------------------------

Texto = ('''Sua chave foi gerada com sucesso segue abaixo \n {} Código Único Pré Encriptado 
 Atenciosamente,Equipe KGP.'''.format(B))
message = Texto

# setup the parameters of the message
password = "Senha do seu Email"
msg['From'] = "Seu Email"
msg['To'] = 'Email para Envio'
msg['Subject'] = 'Reply,Key-Generator'

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("Enviando Para %s:" % (msg['To']))
time.sleep(1)
print('Chave Gerada E Enviada Com Sucesso ')
