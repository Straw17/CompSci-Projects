import smtplib, imapclient, pyzmail

pw = input('Password: ')
sub = input('Subject: ')
body = input('Body: ')
mailingList = ['ejcu8@k12albemarle.org', 'mrsw2@k12albemarle.org']

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('strawbot17@gmail.com', pw)

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
imapObj.login('strawbot17@gmail.com', pw)
imapObj.select_folder('INBOX', readonly = True)
newReports = imapObj.search(['SUBJECT !issue', 'UNSEEN'])
for report in newReports:
    message = pyzmail.PyzMessage.factory(rawMessages[report]['BODY[]'])
    reportText = message.get_subject()
    user =  message.get_addresses('from')
    server.sendmail('strawbot17@gmail.com', user, 'Subject: ' +  + '\n' + body)

#for user in mailingList:
    #server.sendmail('strawbot17@gmail.com', user, 'Subject: ' + sub + '\n' + body)

server.quit()
