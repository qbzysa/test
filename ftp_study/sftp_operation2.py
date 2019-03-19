# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/26 8:37
import pysftp
import os


def connect(host, username, password):
    conpts = pysftp.CnOpts()
    conpts.hostkeys = None
    sf = pysftp.Connection(host=host,
                           username=username,
                           password=password,
                           cnopts=conpts)
    return sf


def disconnect(sf):
    sf.close()


def sftp_upload(sf, local, remote):
    try:
        if os.path.isdir(local): # 判断本地参数是目录还是文件
            for f in os.listdir(local): # 遍历本地目录
                sf.put(os.path.join(local+f), os.path.join(remote+f)) # 上传目录中的文件
        else:
            sf.put(local, remote) # 上传文件
    except Exception, e:
        print('upload exception:', e)


def sftp_download(sf, local, remote):
    try:
        if os.path.isdir(local): # 判断本地参数是目录还是文件
            for f in sf.listdir(remote): # 遍历远程目录
                sf.get(os.path.join(remote+f), os.path.join(local+f)) # 下载目录中文件
        else:
            sf.get(remote, local) # 下载文件
    except Exception, e:
        print('download exception:', e)


if __name__ == '__main__':
    host = '127.0.0.1'
    username = 'mysftp'
    password = '123456'
    sf = connect(host=host, username=username, password=password)
    # 本地文件或目录，与远程一致，当前为windows目录格式，window目录中间需要使用双斜线
    local = 'E:\\sftptest\\'
    # local = "E:\\bcp\\"
    # 远程文件或目录，与本地一致，当前为linux目录格式
    remote = "/upload/"
    # 上传
    sftp_upload(sf, local, remote)
    # 下载
    # sftp_download(sf, local, remote)