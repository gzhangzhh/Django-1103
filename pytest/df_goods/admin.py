# coding=utf-8
from django.contrib import admin
from models import TypeInfo,GoodsInfo

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gkucun','gcontent','gtype']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
#superuser account_data:user,fresh;pwd,123456;email,fresh@163.com.














