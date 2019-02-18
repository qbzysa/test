# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/18 13:33
import os
import shutil
import zipfile
src_dir = "E:\\bcp"
dst_dir = "E:\\bcpback"


def get_files_list(file_dir=None):
    files_list = []
    if file_dir:
        pass
    else:
        file_dir = src_dir
    for root, dirs, files in os.walk(file_dir):
        # print "当前目录路径:%s\n" % root
        # print "当前路径下所有子目录:\n" % dirs
        # print "当前路径下所有非目录子文件:%s" % files
        return files


if __name__ == "__main__":
    file_list = get_files_list(src_dir)
