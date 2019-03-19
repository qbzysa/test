# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 9:34
import paramiko
import os


def connect(host, port, username, password):
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    return sf


def disconnect(sf):
    sf.close()


def sftp_upload(sf, local, remote):
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):#判断本地参数是目录还是文件
            for f in os.listdir(local):#遍历本地目录
                sftp.put(os.path.join(local+f), os.path.join(remote+f))#上传目录中的文件
        else:
            sftp.put(local, remote)#上传文件
    except Exception, e:
        print('upload exception:', e)


def sftp_download(sf, local, remote):
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local): # 判断本地参数是目录还是文件
            for f in sftp.listdir(remote): # 遍历远程目录
                sftp.get(os.path.join(remote+f), os.path.join(local+f)) # 下载目录中文件
        else:
            sftp.get(remote, local) # 下载文件
    except Exception, e:
        print('download exception:', e)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 22
    username = 'mysftp'
    password = '123456'
    sf = connect(host=host, port=port, username=username, password=password)
    # 本地文件或目录，与远程一致，当前为windows目录格式，window目录中间需要使用双斜线
    local = 'E:\\sftptest\\'
    # local = "E:\\bcp\\"
    # 远程文件或目录，与本地一致，当前为linux目录格式
    remote = "/upload/"
    # 上传
    # sftp_upload(sf, local, remote)
    # 下载
    sftp_download(sf, local, remote)