# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/19 14:14
from ftplib import FTP                         # 加载ftp模块
import os
from pika_mq.get_files import get_files_list
sum1 = 0
sum2 = 0
file_size = 0


class Ftp(object):
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = "21"
        self.user = "ftp"
        self.passwd = "123456"
        self.ftp = self.ftp_connect()
        self.files = {}
        self.bufsize = 1024                            # 设置的缓冲区大小

    def ftp_connect(self):
        ftp = FTP()                                    # 生成一个实例
        ftp.set_debuglevel(0)                          # 打开调试级别2，显示详细信息
        ftp.connect(self.host, self.port)              # 连接的ftp sever和端口
        con = ftp.login(self.user, self.passwd)        # 连接的用户名，密码
        if "Login successful" in con:
            print ftp.getwelcome()[4::]                # 打印出欢迎信息
            return ftp
        else:
            print con[4::]

    def search_file(self,  filename=None):
        if filename:
            self.ftp.cwd(filename)
        dir_res = []
        self.ftp.dir('.', dir_res.append)                # 对当前目录进行dir()，将结果放入列表
        for i in dir_res:
            if i.startswith("d"):
                global sum1
                sum1 += 1
                self.search_file(self.ftp.pwd() + "/" + i.split(" ")[-1])
                self.ftp.cwd('..')
            else:
                global sum2, file_size
                sum2 += 1
                one_file = i.split(" ")[-1]
                file_size += self.ftp.size(one_file)
                key = self.ftp.pwd() + "/"+one_file
                value = str(file_size) + "B"
                self.files[key] = value
        return self.files

    def download(self, files, file_path=None):
        for i in files:
            dirs = i.split("/")
            path = ''
            for j in range(0, len(dirs)-1):
                if dirs[j]:
                    path += "\\"+dirs[j]
            dsr_path = file_path+path
            if os.path.exists(dsr_path):
                pass
            else:
                os.makedirs(dsr_path)
            fp = open(dsr_path+'\\'+dirs[-1], 'wb')
            req = self.ftp.retrbinary('RETR %s' % i, fp.write, self.bufsize)
        print req[4::]

    def ftp_disconnect(self):
        req = self.ftp.quit()
        print req

    def uploads(self, file_list):
        self.ftp.cwd("/upload")
        for i in file_list:
            file_handler = open(i, 'rb')
            self.ftp.storbinary('STOR %s' % os.path.basename(i), file_handler, self.bufsize)


if __name__ == "__main__":
    ftp_test = Ftp()
    files = ftp_test.search_file()
    path = "E:\\ftpback"
    # ftp_test.download(files, path)
    file_list = get_files_list()
    print file_list
    ftp_test.uploads(file_list)