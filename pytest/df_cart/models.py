# coding=utf-8
from django.db import models

class CartInfo(models.Model):
    #注意外键关联别的应用的表名，需要加上应用名称限制
    user = models.ForeignKey('df_user.UserInfo')
    goods = models.ForeignKey('df_goods.GoodsInfo')
    count = models.IntegerField()
