#！ -×- coding:utf-8 -*-


import requests
import re
from pymongo import MongoClient






# 尝试用正则 和bs4分别抓取

#传入url,获取响应
def get_one_page(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    html =response.text
    return html




# 解析返回页面 进行字符串拼接

def parse_one_page(html):
    patt = re.compile('.*?<td><a href=".*?">(.*?)</a>'+
                      '.*?<td>(.*?)</td>',re.S)
    items = re.findall(patt,html)
    for i in items:
        yield {
            i[0]:i[1],
        }



        # yield {
        #
        #     'name':i[0],
        #     'theme':i[1],
        # }
        # yield i[0],i[1]   返回的是列表形式




# 导出excel文件  #导出json格式
#  创建到处文档 格式自选  (dict --->>>  str )
# def write_to_file(content):
    #也可以用 csv格式 with open('result.csv','a',encoding='utf-8') as f:
    # a 是追加的方式 json.dumps()是编译json数据，json.loads()是解码json数据
# 把字典形式再转换成字符串的形式   \n 是换行用的 f.write的对象必须是字符串  所以弄到字典再用json整理为str都是套路

    # with open('result.txt','a',encoding='utf-8') as f:
    #     f.write(json.dumps(content,ensure_ascii=False) + '\n')
    #     f.close()
        # 第二种写法  单独一个就可以
    # json.dump(content, open('result.txt', 'a', encoding='utf-8'))

#存入mysql








#存入MongoDB
#
# def insert_to_Mongo(item):
#     client = MongoClient()   #链接连接数据库
#     db = client.R_docs       #建立数据库
#     p = db.themes            #在上面数据库中建立集合（表）
#     result = p.insert(item)  # 添加内容
#     print(result)


def main():
    url = 'https://cloud.r-project.org/web/views/'
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        # insert_to_Mongo(item)
        #  write_to_file(item)




if __name__ == '__main__':
    main()