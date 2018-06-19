#！/usr/bin/env.python
# _*_ coding:utf-8 _*_


import json
import pygal
import math


# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 将每项数据存储到相应的列表中
date = []
month = []
weeks = []
weekday = []
close = []

for btc_dict in btc_data:
    date.append(btc_dict['date'])
    month.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekday.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_label=False,
                        x_labels_major_count=30)
line_chart.title = '收盘价对数变换（元）'
line_chart.x_labels = date
n = 30  # x轴坐标每隔30天显示一次
line_chart.x_labels_major = date[::n]
close_log = [math.log10(i) for i in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价折线图（元）.svg')
