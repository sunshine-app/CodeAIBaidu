# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 9:29
# @Author  : shine
# @File    : code_main.py
from ai_api.ocr_api import get_content_by_path
from ai_sdk.ocr_sdk import general_image
from utils import get_access_token, API_KEY, SECRET_KEY, get_image_content

if __name__ == "__main__":
    # SDK方式
    image_obj = get_image_content('timg.jpg')
    res = general_image(image_obj)
    print(res)

    # API方式
    token = get_access_token(API_KEY, SECRET_KEY)
    content = get_content_by_path('taxi.jpg', token)
    print(content)
