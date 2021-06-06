import smtplib 


SENDER = input("Enter Sender's e-mail:")
PASSWORD = input("Enter Password:")
RECIEVER = input("Enter Reciver's e-mail:")


PORT = 587  
#with open('passwd.txt','r') as passwd:
#    PASSWORD = passwd.read()
#    passwd.close()

SUBJECT = input("Enter Subject:")
#SUBJECT = "Python 3.7 SMPT"
MESSAGE = """Email Automaion through pyhon
\n This email is sent from python automation software and SMTP
\r\n(simple mail transfer protocol).\n\r
which handles sending e-mail and routing between
\n mail servers
"""
MSG = input("""Enter Message: """)

BODY = '\r\n'.join(['To : %s' %RECIEVER,
                    'From : %s' %SENDER,
                    'Subject : %s' %SUBJECT, 
                    '',MSG])


server = smtplib.SMTP('smtp.gmail.com',PORT)
server.ehlo()
server.starttls()
print("[LOGGING...IN]")

server.login(SENDER,PASSWORD)
print("[SENDING....EMAIL]")

server.sendmail(SENDER,RECIEVER,BODY)

print("[EMAIL SENT.]")
server.quit()


