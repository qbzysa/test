# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/12/3 19:21
# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/22 17:38
import os


def classify_file(file, keyword):
    """
    根据关键词分类文件内容到指定的list中
    :param file:
    :return:
    """
    infos = []
    yd = [line.strip().decode('utf-8') for line in open(file).readlines()]
    for qg in yd:
        if keyword in qg:
            infos.append(qg)
    return infos


def write_data(tag, value):
    """
    将tag类型数据写入到指定文件
    :param tag:
    :param value:
    :return:
    """
    file_name = str(tag)+'.txt'
    with open('txt/%s' % file_name, 'w') as f:
        for one in value:
            f.write(one.encode("utf-8"))
            f.write('\n')


if __name__ == "__main__":
    if not os.path.exists('txt'):
        os.mkdir('txt')
    # ####读取分词后的txt文件#######
    keywords = [line.strip().decode('utf-8') for line in open('test.txt').readlines()]
    # ####通过每一个分词生成报告#######
    for key in keywords:
        data = classify_file('yd.txt', key.split(',')[0])
        write_data(key.split(',')[0], data)

