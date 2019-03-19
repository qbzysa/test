# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/7 15:20
import pandas as pd
import time
import datetime
import random
from pyecharts import Line
from pyecharts import Page


def show_by_day(times):
    """
    按日获取实际的时间数据
    :param times: list类型,元素为时间
    :return: Period D
    """
    df = pd.DataFrame()
    df['index'] = pd.to_datetime(times)
    df['number'] = 1
    df_period = df.set_index('index').to_period('D')
    return df_period.reset_index().groupby(by='index').sum().reset_index()


def show_by_week(times):
    """
    按周获取实际的时间数据
    :param times: list类型,元素为时间
    :return: Period W
    """
    df = pd.DataFrame()
    df['index'] = pd.to_datetime(times)
    df['number'] = 1
    df_period = df.set_index('index').to_period('W')
    return df_period.reset_index().groupby(by='index').sum().reset_index()


def show_by_month(times):
    """
    按月获取实际的时间数据
    :param times: list类型,元素为时间
    :return: Period M
    """
    df = pd.DataFrame()
    df['index'] = pd.to_datetime(times)
    df['number'] = 1
    df_period = df.set_index('index').to_period('M')
    return df_period.reset_index().groupby(by='index').sum().reset_index()


def show_by_quarter(times):
    """
    按季度获取实际的时间数据
    :param times: list类型,元素为时间
    :return: Period Q
    """
    df = pd.DataFrame()
    df['index'] = pd.to_datetime(times)
    df['number'] = 1
    df_period = df.set_index('index').to_period('Q')
    return df_period.reset_index().groupby(by='index').sum().reset_index()


def show_by_year(times):
    """
    按年获取实际的时间数据
    :param times: list类型,元素为时间
    :return: Period Y
    """
    df = pd.DataFrame()
    df['index'] = pd.to_datetime(times)
    df['number'] = 1
    df_period = df.set_index('index').to_period('Y')
    return df_period.reset_index().groupby(by='index').sum().reset_index()


def standard_by_day(start, end):
    """
    按日获取标准的时间数据
    :param start:
    :param end:
    :return:
    """
    standard_day = pd.DataFrame(pd.date_range(start, end).to_period('D').drop_duplicates(),
                                columns=['index'])
    return standard_day


def standard_by_week(start, end):
    """
    按周获取标准的时间数据
    :param start:
    :param end:
    :return:
    """
    standard_week = pd.DataFrame(pd.date_range(start, end).to_period('W').drop_duplicates(),
                                 columns=['index'])
    return standard_week


def standard_by_month(start, end):
    """
    按月获取标准的时间数据
    :param start:
    :param end:
    :return:
    """
    standard_month = pd.DataFrame(pd.date_range(start, end).to_period('M').drop_duplicates(),
                                  columns=['index'])
    return standard_month


def standard_by_quarter(start, end):
    """
    按季度获取标准的时间数据
    :param start:
    :param end:
    :return:
    """
    standard_quarter = pd.DataFrame(pd.date_range(start, end).to_period('Q').drop_duplicates(),
                                    columns=['index'])
    return standard_quarter


def standard_by_year(start, end):
    """
    按年获取标准的时间数据
    :param start:
    :param end:
    :return:
    """
    standard_year = pd.DataFrame(pd.date_range(start, end).to_period('Y').drop_duplicates(),
                                 columns=['index'])
    return standard_year


if __name__ == "__main__":
    a1 = (1999, 1, 1, 0, 0, 0, 0, 0, 0)
    a2 = (2018, 8, 7, 23, 59, 59, 0, 0, 0)
    start = time.mktime(a1)
    end = time.mktime(a2)
    times = []
    for i in range(100):
        t = random.randint(start, end)                 # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)                # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        times.append(date)
    localtime = datetime.datetime.now().strftime('%Y-%m-%d')
    page = Page()  # 实例化，同一网页按顺序展示多图
    day = show_by_day(times)
    standard_day = standard_by_day('2017-04-19', localtime)
    line = Line('按日统计图', title_pos='center')
    day_test = pd.merge(standard_day, day, how='outer', on=['index']).drop_duplicates().sort_values(by=['index']).fillna(0)
    line.add(None,
             day_test['index'].values[::-1][:20],
             day_test['number'].values[::-1][:20],
             xaxis_rotate=45)
    page.add(line)

    week = show_by_week(times)
    standard_week = standard_by_week('2017-04-19', localtime)
    line = Line('按周统计图', title_pos='center')
    week_test = pd.merge(standard_week, week, how='outer', on=['index']).drop_duplicates().sort_values(by=['index']).fillna(0)
    line.add(None,
             week_test['index'].values[::-1][:20],
             week_test['number'].values[::-1][:20],
             xaxis_rotate=45)
    page.add(line)

    month = show_by_month(times)
    standard_month = standard_by_month('2017-04-19', localtime)
    line = Line('按月统计图', title_pos='center')
    month_test = pd.merge(standard_month, month, how='outer', on=['index']).drop_duplicates().sort_values(by=['index']).fillna(0)
    line.add(None,
             month_test['index'].values[::-1][:20],
             month_test['number'].values[::-1][:20],
             xaxis_rotate=45)
    page.add(line)

    quarter = show_by_quarter(times)
    standard_quarter = standard_by_quarter('2017-04-19', localtime)
    line = Line('按季度统计图', title_pos='center')
    quarter_test = pd.merge(standard_quarter, quarter, how='outer', on=['index']).drop_duplicates().sort_values(by=['index']).fillna(0)
    line.add(None,
             quarter_test['index'].values[::-1][:20],
             quarter_test['number'].values[::-1][:20],
             xaxis_rotate=45)
    page.add(line)

    year = show_by_year(times)
    standard_year = standard_by_year('2017-04-19', localtime)
    line = Line('按年统计图', title_pos='center')
    year_test = pd.merge(standard_year, year, how='outer', on=['index']).drop_duplicates().sort_values(by=['index']).fillna(0)
    line.add(None,
             year_test['index'].values[::-1][:20],
             year_test['number'].values[::-1][:20],
             xaxis_rotate=45)
    page.add(line)
    page.render(r'E:\echart\time_echart.html')