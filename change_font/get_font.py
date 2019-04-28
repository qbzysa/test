# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/4/26 11:36

from fontTools.ttLib import TTFont
import re
import os


def get_font(woff='4DOqcP.woff'):
    font = TTFont(woff)

    font.saveXML(woff.split('/')[-1]+'.xml')
    with open(woff.split('/')[-1]+'.xml', 'r') as f:
        xml = f.read()
    GlyphID = re.findall(r'<GlyphID id="(.*?)" name="(.*?)"/>', xml)
    temp = {}
    for Gid, Gname in GlyphID:
        # 通过FontCreator查看woff,发现web上面的字体数字与woff的映射字体数字相差少一
        temp[Gname] = int(Gid)-1
    os.remove(woff)
    os.remove(woff.split('/')[-1]+'.xml')
    return temp


if __name__ =="__main__":
    get_font()