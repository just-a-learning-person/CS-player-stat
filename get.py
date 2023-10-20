import pandas as pd

io = "D:\wangshuotest\CS-player-stat\datatest\Counter-Strike Player statistics database _ HLTV.org.html"

datalist = pd.DataFrame()

datalist=datalist.append(pd.read_html(io),ignore_index=True)
datalist.to_csv('D:\\wangshuotest\\CS-player-stat\\data.csv')