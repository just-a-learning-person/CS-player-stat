import pandas as pd
import urllib
import urllib.request

# datalist=datalist.append(pd.read_html(io),ignore_index=True)

# 返回这个datalist没用，我们需要每个选手的详细信息，而且这还是用下载下来的html做的

# datalist.to_csv('D:\\wangshuotest\\CS-player-stat\\data.csv')

# 定义爬取网页函数
def get_page_html(event_number):
    url = "https://www.hltv.org/stats/players?event="
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers)
    return urllib.request.urlopen(req).read()   # TypeError: can't concat str to bytes

def set_table(html,filepath):
    datalist = pd.DataFrame().append(pd.read_html(html),ignore_index=True)
    datalist.to_csv(filepath)
    

if __name__=='__main__':
    # 本地测试数据路径
    # io = "D:\wangshuotest\CS-player-stat\datatest\Counter-Strike Player statistics database _ HLTV.org.html"
    input_event_number = input("event_number: ")
    page_html = get_page_html(input_event_number)
    print(page_html)
    datable = set_table(page_html, 'D:\\wangshuotest\\CS-player-stat\\data1.csv')