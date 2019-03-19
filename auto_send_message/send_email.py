# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/21 10:46
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def email_test():
    smtp = smtplib.SMTP()
    smtp.connect('mail.pansafe.com', 25)
    smtp.login('qiubenzhao@pansafe.com', '8yD2WwRa3A')
    # 邮件内容
    mail_subject = "python发送邮件测试"         # 邮件的标题
    mail_context = "这是邮件内容"

    msg = MIMEMultipart()
    msg["From"] = 'qiubenzhao@pansafe.com'  # 发件人
    msg["To"] = '2541183419@qq.com'  # 收件人
    msg["Subject"] = mail_subject   # 邮件标题
    # 邮件正文
    msg.attach(MIMEText(mail_context, 'plain', 'utf-8'))
    # 图片附件
    # 不同的目录下要写全文件路径
    with open('E:\\autotest\\result\\image\\2018-12-26\\2018-12-26-10_22_11.png', 'rb') as picAtt:
        msgImg = MIMEImage(picAtt.read())
        msgImg.add_header('Content-Disposition', 'attachment', filename="test.png")
        msg.attach(msgImg)

    # 构造附件
    att = MIMEText(open('E:\\autotest\\result\\SoftTestReport_2018-12-26-10_20_20.html', "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    # 附件名称
    att.add_header("Content-Disposition", "attachment", filename="test.html")
    msg.attach(att)

    smtp.sendmail('qiubenzhao@pansafe.com', '2541183419@qq.com', msg.as_string())
    smtp.quit()


def email_test2():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('2541183419@qq.com', 'bjohabvbvccdebhi')
    # 邮件内容
    mail_subject = "python发送邮件测试"  # 邮件的标题
    mail_context = "这是邮件内容"

    msg = MIMEMultipart()
    msg["From"] = '2541183419@qq.com'  # 发件人
    msg["To"] = 'qiubenzhao@pansafe.com'  # 收件人
    msg["Subject"] = mail_subject  # 邮件标题
    # 邮件正文
    msg.attach(MIMEText(mail_context, 'plain', 'utf-8'))
    # 图片附件
    # 不同的目录下要写全文件路径
    with open('E:\\autotest\\result\\image\\2018-12-26\\2018-12-26-10_22_11.png', 'rb') as picAtt:
        msgImg = MIMEImage(picAtt.read())
        msgImg.add_header('Content-Disposition', 'attachment', filename="test.png")
        msg.attach(msgImg)

    # 构造附件
    att = MIMEText(open('E:\\autotest\\result\\SoftTestReport_2018-12-26-10_20_20.html', "rb").read(), "base64",
                   "utf-8")
    att["Content-Type"] = "application/octet-stream"
    # 附件名称为中文时的写法
    att.add_header("Content-Disposition", "attachment", filename="test.html")
    # 附件名称非中文时的写法
    # att["Content-Disposition"] = 'attachment; filename="test.html")'
    msg.attach(att)

    smtp.sendmail('2541183419@qq.com', 'qiubenzhao@pansafe.com', msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    email_test2()