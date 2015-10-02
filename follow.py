#! encoding=utf-8

__author__ = 'zhufb'

import requests
import base64
import re
import rsa
import urllib
import json
import binascii
import time

session = requests.Session()
cookie = '__gads=ID=7363ea48196f40d4:T=1443600612:S=ALNI_MYz_XlrDMt6sJGPMSZ7WcOZSBjKvQ; YF-Ugrow-G0=169004153682ef91866609488943c77f; SUS=SID-2636688737-1443752366-GZ-wiboy-8e250b1cc292a75d92e374f24a56bd03; SUE=es%3D773ba137980cc77bd3a239e66250e8f0%26ev%3Dv1%26es2%3D49cf99903fc619dc0ff1dcf1a3030763%26rs0%3DXNJELqnz9b6nu%252BcC71LjYHPXAv7cudSr1OqWl3bBoj6NjWeJFYp8cREsdRAo1PBU2CZ0tptg6fc4ASxp8EA0oYZxdfArzhhV5tD%252BqPrs3FCce%252BND286lj3Etya0WeFC0roALUkyd%252FrViXOgao6PkT27MwSYMcSUB3UpYijb0w80%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1443752366%26et%3D1443838766%26d%3Dc909%26i%3Dbd03%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2636688737%26name%3Dqazmichaelgw%2540gmail.com%26nick%3Dmichael%26fmp%3D%26lcp%3D; SUB=_2A257CZn-DeTxGeRI6FQX-CbLyDuIHXVYfow2rDV8PUJbuNBuLWXTkW8Y5Oqn2D3JKq9BJQw7Z3j-3_ddJA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whn-qSkuoS2guFQsIQf.uTZ5JpX5K2t; SUHB=0eb8jswcBF18U4; SSOLoginState=1443752366; _ga=GA1.2.1477948635.1443600613; lang=en-us; wvr=6; YF-V5-G0=dc2e98bae9c8f3ecec40249231d366d6; YF-Page-G0=c81c3ead2c8078295a6f198a334a5e82; _s_tentry=weibo.com; Apache=739994028117.5077.1443752531439; SINAGLOBAL=739994028117.5077.1443752531439; ULV=1443752531556:1:1:1:739994028117.5077.1443752531439:; UOR=,,www.google.com.sg'

# uid:1257818405
# objectid:
# f:0
# extra:
# refer_sort:friends
# refer_flag:dynamic
# location:friends_dynamic
# oid:2904827730
# wforce:1
# nogroup:1
# fnick:贾乃亮
# template:2
# third_appkey_alias:attfeed
# _t:0
#usage: followed(your_own_uid, target_uid)
def follow(oid,dstuid):
        followedurl = "http://weibo.com/aj/f/followed?ajwvr=6&__rnd=%s"% int(time.time())
        data = {
            'uid':dstuid,
            'objectid':'',
            'f':0,
            'extra':'',
            'refer_sort':'friends',
            'refer_flag':'dynamic',
            'location':'friends_dynamic',
            'oid':oid,
            'nogroup':1,
            'template':2,
            'wforce':1,
            'third_appkey_alias':'attfeed',
            '_t':0,
        }
        ref = 'http://weibo.com/u/'+ str(oid) + '/home'
        headers = {}
        headers['Cookie'] = cookie
        headers['Referer'] = ref
        respon = session.post(followedurl, data, headers=headers)
        print respon.status_code
        print respon.text

follow(2636688737,1649166140)
def unfollow(oid,dstuid):
        followedurl = "http://weibo.com/aj/f/unfollow?ajwvr=6&__rnd=%s"% int(time.time())
        data = {
            'uid':dstuid,
            'objectid':'',
            'f':0,
            'extra':'',
            'refer_sort':'friends',
            'refer_flag':'dynamic',
            'location':'friends_dynamic',
            'oid':oid,
            'nogroup':1,
            'template':2,
            'wforce':1,
            'third_appkey_alias':'attfeed',
            '_t':0,
        }
        ref = 'http://weibo.com/u/'+ str(oid) + '/home'
        headers = {}
        headers['Cookie'] = cookie
        headers['Referer'] = ref
        respon = session.post(followedurl, data, headers=headers)
        print respon.status_code
        print respon.text

#unfollow(2636688737,1649166140)
