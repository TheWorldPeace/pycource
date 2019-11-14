import csv
import smtplib
from email.mime.text import MIMEText


def send_mail(to_list, sub, content):
    mail_host = "smtp.163.com"
    mail_user = "XXXX@163.com"
    mail_pass = "XXXX"
    mail_postfix = "163.com"
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == '__main__':
    with open('email.csv') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print(row[1])
            if send_mail(row[1], "hello world", "python test email"):
                print("发送成功")
            else:
                print("发送失败")
