# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BaiheItem(scrapy.Item):
    mongodb_id = Field()
    name = Field()
    baiheid = Field()#id
    avatar = Field()#头像
    description = Field()#描述
    age = Field()#年龄
    height = Field()#身高
    weight = Field()#体重
    education = Field()#教育程度
    lovetype = Field()#恋爱类型
    img = Field()#图片
    address = Field()#现居地
    income = Field()#收入
    marriage=Field()#婚姻
    self_evaluation=Field()#自我评价
    account=Field()#户口
    occupation=Field()#职业
    profession=Field()#专业
    familysituation=Field()#家庭情况
    parentalstatus=Field()#父母情况
    motherwork=Field()#母亲工作
    fatherwork=Field()#父亲工作
    marriagetime=Field()#结婚时间
    dating=Field()#约会方式
    otherfancy=Field()#对方看中
    cooking=Field()#厨艺状态

    manage=Field()#对方年龄
    manheight = Field()  # 对方身高
    manedu = Field()  # 对方学历
    manincome = Field()  # 对方收入
    manaddress = Field()  # 对方所在地

    hobbies=Field()#爱好
    bodytype=Field()#体型


    pass
