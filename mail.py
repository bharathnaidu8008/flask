# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:33:11 2020

@author: ARJUN
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(firstname, lastname, username, mailid):
    mail_content = f'''Hi {firstname} {lastname},
    
    Heartful welcome to Bharath University. Your signup done successfully your login Id: {username}
    
    Thanks,
    Bharath University
    '''
    # The mail addresses and password
    sender_address = 'naidugoutham66@gmail.com'
    sender_pass = 'pratubharath'
    receiver_address = mailid
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Bharath University'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')