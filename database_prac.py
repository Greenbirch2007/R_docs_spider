

from pymongo import MongoClient
def insert_to_Mongo(item):
    client = MongoClient()   #链接连接数据库
    db = client.R_docs       #建立数据库
    p = db.themes            #在上面数据库中建立集合（表）
    result = p.insert(item)  # 添加内容
    print(result)

item = {
    'id':'00001',

}


insert_to_Mongo(item)