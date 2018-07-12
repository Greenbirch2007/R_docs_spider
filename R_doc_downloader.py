#-*- coding:utf-8 -*-

# 保存pdf文件


proxies = {"https":"https://118.31.220.3"}

import requests
import re 
from lxml import etree
from bs4 import BeautifulSoup

# /html/body/ul[1]/li[1]/a
# /html/body/ul[1]/li[2]/a  

def get_all_links(url):
	response = requests.get(url,timeout=10)
	return response.text



Bayesian=[]
ChemPhys=[]
ClinicalTrials=[]
Cluster=[]
DifferentialEquations=[]
Distributions=[]
Econometrics=[]
Environmetrics=[]
ExperimentalDesign=[]
ExtremeValue=[]
Finance=[]
FunctionalData=[]
Genetics=[]
Graphics=[]
HighPerformanceComputing=[]
MachineLearning=[]
MedicalImaging=[]
MetaAnalysis=[]
ModelDeployment=[]
Multivariate=[]
NaturalLanguageProcessing=[]
NumericalMathematics=[]
OfficialStatistics=[]
Optimization=[]
Pharmacokinetics=[]
Phylogenetics=[]
Psychometrics=[]
ReproducibleResearch=[]
Robust=[]
SocialSciences=[]
Spatial=[]
SpatioTemporal=[]
Survival=[]
TimeSeries=[]
WebTechnologies=[]
gR=[]


# 解析的部分

# url ="https://cloud.r-project.org/web/views/"



"""
https://cloud.r-project.org/web/views/Bayesian.html
https://cloud.r-project.org/web/views/ChemPhys.html
https://cloud.r-project.org/web/views/ClinicalTrials.html
https://cloud.r-project.org/web/views/Cluster.html
https://cloud.r-project.org/web/views/DifferentialEquations.html
https://cloud.r-project.org/web/views/Distributions.html
https://cloud.r-project.org/web/views/Econometrics.html
https://cloud.r-project.org/web/views/Environmetrics.html
https://cloud.r-project.org/web/views/ExperimentalDesign.html
https://cloud.r-project.org/web/views/ExtremeValue.html
https://cloud.r-project.org/web/views/Finance.html
https://cloud.r-project.org/web/views/FunctionalData.html
https://cloud.r-project.org/web/views/Genetics.html
https://cloud.r-project.org/web/views/Graphics.html
https://cloud.r-project.org/web/views/HighPerformanceComputing.html
https://cloud.r-project.org/web/views/MachineLearning.html
https://cloud.r-project.org/web/views/MedicalImaging.html
https://cloud.r-project.org/web/views/MetaAnalysis.html
https://cloud.r-project.org/web/views/ModelDeployment.html
https://cloud.r-project.org/web/views/Multivariate.html
https://cloud.r-project.org/web/views/NaturalLanguageProcessing.html
https://cloud.r-project.org/web/views/NumericalMathematics.html
https://cloud.r-project.org/web/views/OfficialStatistics.html
https://cloud.r-project.org/web/views/Optimization.html
https://cloud.r-project.org/web/views/Pharmacokinetics.html
https://cloud.r-project.org/web/views/Phylogenetics.html
https://cloud.r-project.org/web/views/Psychometrics.html
https://cloud.r-project.org/web/views/ReproducibleResearch.html
https://cloud.r-project.org/web/views/Robust.html
https://cloud.r-project.org/web/views/SocialSciences.html
https://cloud.r-project.org/web/views/Spatial.html
https://cloud.r-project.org/web/views/SpatioTemporal.html
https://cloud.r-project.org/web/views/Survival.html
https://cloud.r-project.org/web/views/TimeSeries.html
https://cloud.r-project.org/web/views/WebTechnologies.html
https://cloud.r-project.org/web/views/gR.html
"""


# html = get_all_links(url)
# selector=etree.HTML(html)
# names = selector.xpath("/html/body/ul[1]/li//text()")
# print(names)

# 这个地方尝试使用bs4 
# html = get_all_links(url)
# patt = re.compile('<td><a href=".*?">(.*?)</a></td>')
# items = re.findall(patt,html)
# for i in items:
# 	print('https://cloud.r-project.org/web/views/'+i + '.html')

# for i in names:
# 	Finance.append(i)
	
# print(Finance)

 # 尝试来一个列表

# /html/body/table/tbody/tr[1]/td[1]/a
# /html/body/table/tbody/tr[1]/td[2]
# /html/body/table/tbody/tr[2]/td[1]/a



# url ="https://cloud.r-project.org/web/views/Bayesian.html"
# html =get_all_links(url)
# selector=etree.HTML(html)
# names = selector.xpath("/html/body/ul[1]/li//text()")
# for i in names:
# 	pdf_link ="https://cloud.r-project.org/web/packages/"+  i+ "/" +i + ".pdf"





# pdf 文件下载
def getFile(url):
	u = requests.get(url)
	if u.response.status_code == 200:
		s = 0   # 命名是一个很费劲的事！能省则省
		with open("E:\\ %s .pdf" % s ,"wb") as f:
			f.write(u.content)
			f.close()
		s += 1
	else:
		pass


url = "https://cloud.r-project.org/web/packages/abc/abc.pdf"
getFile(url)



# https://cloud.r-project.org/web/packages/abc/abc.pdf  # 文件的链接


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
#     client = MongoClient(host='localhost',port=27017)   #链接连接数据库
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










# 用得到的主题名称的遍历元素作为命名



# if __name__ == "__main__":
# 	url = "https://cloud.r-project.org/web/packages/fTrading/fTrading.pdf"
# 	getFile(url)
