# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 16:30
# @Author  : shine
# @File    : ocr_api.py
import base64
import json
import requests
from utils import get_image_content


def get_content_by_path(image_path, access_token):
    return get_content_image(image_path, None, access_token)


def get_content_by_url(image_url, access_token):
    return get_content_image(None, image_url, access_token)


def get_content_image(image_path, image_url, access_token):
    api_ocr_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # api_ocr_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/taxi_receipt"
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'access_token': access_token
    }
    if image_path:
        image = get_image_content(image_path)
        data['image'] = base64.standard_b64encode(image)
    else:
        data['url'] = image_url

    response = requests.post(url=api_ocr_url, data=data, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content, encoding='utf-8')
    else:
        return None
