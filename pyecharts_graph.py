#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:43:02 2019

@author: Cyan
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Author:  Linxy -- <592901071@qq.com>
  Created: 2017-7-30
"""


from pyecharts.charts.basic_charts.graph import Graph
#引用之前要先pip install pyecharts及相关的支持模块


nodes = [{"name": "外网", "symbolSize": 50,'symbol':'/Users/Cyan/Desktop/point.png'},#注意图标的位置要用绝对地址，否则会认不到图片
         {"name": "防火墙", "symbolSize": 40},#设置节点及节点图标大小
         {"name": "核心交换", "symbolSize": 50},
         {"name": "9-A1-1", "symbolSize": 20},
         {"name": "9-A1-2", "symbolSize": 20},
         {"name": "9-A1-3", "symbolSize": 20},
         {"name": "9-A3-1", "symbolSize": 20},
         {"name": "9-A3-2", "symbolSize": 20},         
         {"name": "9-A3-3", "symbolSize": 20},]

links = [{"source": "防火墙", "target": "外网"},#设置节点连接关系
         {"source": "防火墙", "target": "核心交换"},
         {"source": "核心交换", "target": "9-A1-1"},
         {"source": "核心交换", "target": "9-A1-2"},
         {"source": "核心交换", "target": "9-A1-3"},
         {"source": "核心交换", "target": "9-A3-1"},
         {"source": "核心交换", "target": "9-A3-2"},
         {"source": "核心交换", "target": "9-A3-3"},]

graph = Graph()#画布高600宽800
graph.add("", nodes, links)#is_label_show=True表示节点名字为一直显示
#graph.show_config()#表示将生成的文件打印出来，我们只要结果的HTML不需要知道代码
graph.render(r'./tb.html')#生成html文件并保存到当前路劲下。




