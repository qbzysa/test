# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/29 8:59
import jieba.analyse


def get_analyse_data(src_file):
    """
    将文件进行结巴分词，并记录权重
    :param src_file: 源文件
    :return:
            dict_infos  分词结果
            weights    权重数
    """
    infos = open(src_file, "r").read()
    dict_infos = {}
    fenci = jieba.cut_for_search(infos)

    for fc in fenci:
        if fc in dict_infos:
            dict_infos[fc] += 1
        else:
            dict_infos.setdefault(fc, 1)
    weights = jieba.analyse.extract_tags(infos, topK=50)
    return dict_infos, weights


def write_data(infos, weights, keys, dst_file):
    """
    将分词结果经过指定条件过滤，并保存
    :param infos:     分词结果
    :param weights:   权重数
    :param keys:      过滤key列表
    :param dst_file:  目的文件
    :return:
    """
    with open(dst_file, "w") as f:
        for qg in weights:
            if qg in keys:
                pass
            else:
                print qg + "," + str(infos[qg])
                f.write(qg.encode("utf-8") + "," + str(infos[qg]))
                f.write('\n')


if __name__ == "__main__":
    # ###########获取过滤条件列表############
    stopkey = [line.strip().decode('utf-8') for line in open('stopkey.txt').readlines()]
    data, weight = get_analyse_data('yd.txt')
    write_data(data, weight, stopkey, 'test.txt')