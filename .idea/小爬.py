import requests
import parsel
url="https://163.wmbk.net/index/console/netease/info/299079383"
headers="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"
response=requests.get(url, headers)
print(response.text)
#解析数据
selector =parsel.Selector(response.text)
# css选择器 根据标签选择内容
list=selector.css('fs-sm')
for li in list:
    print(li)