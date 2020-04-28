import smtplib
for i in range(101):
    content = "Life is Tough."
    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.starttls()
    mail.login('Gilfoyle69@gmail.com','Wewake@28')
    mail.sendmail ('Gilfoyle69@gmail.com','wewakeprasad@gmail.com',content)
    mail.close()
    print("Email sent : ",i)
