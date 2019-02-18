# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/16 11:31
import os
import zipfile
import gzip
import tarfile


# 解压zip包
def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    new_file_dir = file_name.split(".zip")[0]
    if os.path.isdir(new_file_dir):
        pass
    else:
        os.mkdir(new_file_dir)
    for names in zip_file.namelist():
        zip_file.extract(names, new_file_dir)
    zip_file.close()
    # os.remove(file_name)
    return new_file_dir


# 解压tar包
def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    new_file_dir = file_name.split(".tar")[0]
    if os.path.isdir(new_file_dir):
        pass
    else:
        os.mkdir(new_file_dir)
    # 因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, new_file_dir)
    tar.close()
    # os.remove(file_name)
    return new_file_dir


# 解压gz包
def un_gz(file_name):
    f_name = file_name.replace(".gz", "")
    # 获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    # 创建gzip对象
    open(f_name, "w+").write(g_file.read())
    # gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    # 关闭gzip对象
    return f_name


if __name__ == "__main__":
    un_zip_dir = un_zip("C:\Users\Administrator\Desktop\\137-736651367-320100-310000-1492594413-00001.zip")
    un_tar_dir = un_tar("C:\Users\Administrator\Desktop\\2018.4.17 16_56\pip-9.0.1.tar.gz")

