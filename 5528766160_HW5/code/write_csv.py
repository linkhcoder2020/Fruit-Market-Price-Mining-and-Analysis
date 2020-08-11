# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         write_csv
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------
from __future__ import unicode_literals
import csv
from config import HEADER


def write_to_csv(filepath, all_data):
    """
    存进csv文件
    :param filepath: csv路径
    :param all_data: 所有水果数据
    :return:
    """
    with open(filepath, 'w') as ff:
        csv_writer = csv.writer(ff)
        csv_writer.writerow(HEADER)
        csv_writer.writerows(all_data)
    print('write csv done')


# if __name__ == '__main__':
#     write_to_csv('./test_data.csv', [['1', '2', '3'], [2, 2, 3]])
