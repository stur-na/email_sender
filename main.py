#import the required module
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#connect to an smtp server and start the server with the right authentication
server = smtplib.SMTP('your email server address', port)
server.starttls()

#load the password file
with open('your_password_file.txt', 'r') as f:
    your_password = f.read()

#login to server
server.login('your email address', your_password)

#set the headers of the email using mimemultipart(can be treated as a dictionary)
msg = MIMEMultipart()
msg['from'] = 'Your name or address'
msg['to'] = 'receiver address'
msg['subject'] = 'message subject'

#load the message file
with open('your_message_body.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

#add and load the attachment
filename = 'your_file.jpg'
attachment = open(filename, 'rb')

#encode and add the attachment to the main message to be sent
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('content-disposition', f'attachment; filename={filename}')
msg.attach(p)
text = msg.as_string()

#send the email
server.sendmail('your_email_address', 'receiver_address', text)
#close the smtp connection
server.quit()
