# CS-player-stat

## 一个提取CS职业选手比赛数据的小程序demo

想法是用python的网页信息提取功能，对"https://www.hltv.org/stats/players?event=6865"进行爬取。event作为一个输入参数，选择不同的比赛。

要有一个前端页面，可以是简单的exe

输入比赛编号6865

输出路径：”     “

内部逻辑：

1. 访问比赛数据页https://www.hltv.org/stats/players?event=6865
2. 保存所有选手的数据详情网页，包括html代码和素材库