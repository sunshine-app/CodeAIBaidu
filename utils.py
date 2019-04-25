# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 16:36
# @Author  : shine
# @File    : utils.py
import json
import requests

""" 你的 APPID AK SK """
# 你的 App ID
APP_ID = '16090176'
# 你的 Api Key
API_KEY = 'Om6MTZMg1KbyznFzE1BMgl18'
# 你的 Secret Key
SECRET_KEY = 'EMnAzzi7pp4lmxzspwOejcEMB9YNFVvz'

options = {
    "language_type": "CHN_ENG",
    "detect_direction": "true",
    "detect_language": "true",
    "probability": "true"
}


def get_image_content(image_path):
    with open(image_path, 'rb') as fp:
        return fp.read()


def get_access_token(client_id, client_secret):
    """ client_id 为官网获取的AK， client_secret 为官网获取的SK """
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    url_param = "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}".\
        format(client_id=client_id, client_secret=client_secret)
    url = "https://aip.baidubce.com/oauth/2.0/token?{url_param}".format(url_param=url_param)

    response = requests.post(url=url, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content, encoding='utf-8')
        return content['access_token']
    else:
        return None


def get_authorization():
    pass
