#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : qtwang
# @Email : qtwang315518@163.com
# @Time : 2020-9-2 14:42
#https://github.com/yannforget/pylandsat
from datetime import datetime

from shapely.geometry import Point
from pylandsat import Catalog, Product

catalog = Catalog()

begin = datetime(2020, 7, 20)
end = datetime(2020, 9, 4)
path=[121,122]
row=[47,48]
# geom = Point(4.34, 50.85)

# Results are returned as a list
# scenes = catalog.search(
#     begin=begin,
#     end=end,
#     geom=geom,
#     sensors=['ETM', 'LC08']
# )

scenes = catalog.search(begin=begin,end=end,path=path,row =row,sensors=['LE07', 'LC08'],maxcloud=100)
print("共查询到%s景数据,即将开始下载！"%(len(scenes)))
for scene in scenes:
    product_id = scene['product_id']
    # Download the scene
    product = Product(product_id)
    product.download(out_dir='data')
