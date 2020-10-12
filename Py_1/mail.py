import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='classarjun@gmail.com'
to_addr=['vankaniarjun0103@gmail.com','mshah5225@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='You will be hack'

body='Your password must be check'

msg.attach(MIMEText(body,'plain'))

email='classarjun@gmail.com'
password='#'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()