# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 16:30
# @Author  : shine
# @File    : ocr_sdk.py
from aip import AipOcr
from utils import APP_ID, API_KEY, SECRET_KEY

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def general_image(image, options=None):
    """ 调用通用文字识别, 图片参数为本地图片 """
    if options is None:
        return client.basicGeneral(image)
    else:
        # 带参数
        return client.basicGeneral(image, options)


def general_image_url(url, options=None):
    """ 调用通用文字识别, 图片参数为远程url图片 """
    if options is None:
        return client.basicGeneralUrl(url)
    else:
        # 带参数
        return client.basicGeneralUrl(url, options)
