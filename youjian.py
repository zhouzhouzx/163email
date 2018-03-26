#encoding:utf-8
__author__ = 'zhouxuan-s'

import smtplib
from email.mime.text import MIMEText


mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
port=25         # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
mail_user="15810918159"                           #用户名
mail_pass="zx3256"                             #密码
mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com
mailto_list=['1934337268@qq.com']           #收件人(列表)

def send_mail(receiver,sub,content):
    sender="test163"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = ";".join(receiver)                #将收件人列表以‘；’分隔

    server = smtplib.SMTP()
    server.connect(mail_host,port)                            #连接服务器
    server.login(mail_user,mail_pass)               #登录操作
    server.sendmail(sender, receiver, msg.as_string())
    server.close()


for i in range(1):                             #发送1封，上面的列表是几个人，这个就填几
    sub='主题是：测试163邮箱'
    content='邮件正文\n发送内容'
    if send_mail(mailto_list,sub,content):  #邮件主题和邮件内容
        #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print ("done!")
    else:
        print ("failed!")

