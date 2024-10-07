import smtplib

# Create an SMTP object and establish a connection to the SMTP server
smtpObj = smtplib.SMTP('smtp.example.com', 25)

# Identify yourself to an ESMTP server using EHLO
smtpObj.ehlo()

# Secure the SMTP connection
smtpObj.starttls()

# Login to the server (if required)
smtpObj.login('username', 'password')

# Send an email
from_address = 'your_email@example.com'
to_address = 'recipient@example.com'
message = """\
Subject: Test Email

This is a test email message.
"""

smtpObj.sendmail(from_address, to_address, message)

# Quit the SMTP session
smtpObj.quit()

import smtplib


def prompt(prompt):
    return input(prompt).strip()


fromaddr = prompt("From: ")
toaddrs = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))
server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['From'] = 'From Person <from@fromdomain.com>'
msg['To'] = 'To Person <to@todomain.com>'
msg['Subject'] = 'SMTP HTML e-mail test'

# HTML message content
html = """\
<html>
  <head></head>
  <body>
    <p>This is an e-mail message to be sent in <b>HTML format</b></p>
    <p><b>This is HTML message.</b></p>
    <h1>This is headline.</h1>
  </body>
</html>
"""

# Attach HTML content to the email
part2 = MIMEText(html, 'html')
msg.attach(part2)

# Connect to SMTP server and send email
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, msg.as_string())
   print("Successfully sent email")
except smtplib.SMTPException as e:
   print(f"Error: unable to send email. Error message: {str(e)}")

import smtplib
import base64

filename = "/tmp/test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'webmaster@tutorialpoint.com'
reciever = 'amrood.admin@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachment.
"""
# Define the main headers.
part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachment
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, reciever, message)
   print("Successfully sent email")
except Exception:
   print ("Error: unable to send email")

import smtplib

# Email content
content = "Hello World"

# Set up SMTP connection to Gmail's SMTP server
mail = smtplib.SMTP('smtp.gmail.com', 587)
# Identify yourself to the SMTP server
mail.ehlo()
# Start TLS encryption for the connection
mail.starttls()

# Gmail account credentials
sender = 'your_email@gmail.com'
password = 'your_password'

# Login to Gmail's SMTP server
mail.login(sender, password)

# Email details
recipient = 'recipient_email@example.com'
subject = 'Test Email'

# Construct email message with headers
header = f'To: {recipient}\nFrom: {sender}\nSubject: {subject}\n'
content = header + content

# Send email
mail.sendmail(sender, recipient, content)

# Close SMTP connection
mail.quit()