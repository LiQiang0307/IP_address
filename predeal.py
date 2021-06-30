'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-06-29 21:31:18
LastEditTime: 2021-06-30 08:42:45
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑       永不宕机     永无BUG

       佛曰:  
               写字楼里写字间，写字间里程序员；  
               程序人员写程序，又拿程序换酒钱。  
               酒醒只在网上坐，酒醉还来网下眠；  
               酒醉酒醒日复日，网上网下年复年。  
               但愿老死电脑间，不愿鞠躬老板前；  
               奔驰宝马贵者趣，公交自行程序员。  
               别人笑我忒疯癫，我笑自己命太贱；  
               不见满街漂亮妹，哪个归得程序员？
'''

'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-06-29 21:31:18
LastEditTime: 2021-06-29 21:49:02
'''
"""
&userSID=  //用户的访问ID，可以使用session id，未登录用户也有访问id
&userUIP=  //用户的ip地址，js/手机端请求可以为空，服务器端请求必须填写
&actionClient=  //用户的客户端
&actionBegin=  //用户动作开始时间，可以为空
&actionEnd=  //用户动作结束时间，不能为空
&actionType=  //用户动作分类，比如"互动行为"，"用户行为"
&actionName=  //用户动作名字，比如"发布帖子"，"用户注册"
&actionValue=  //用户动作内容，比如"帖子编号"，下方说明
&actionPrepend=  //用户动作前置，比如"从什么课程跳转到注册界面"
&actionTest=  //是否是测试动作  0:正式；1：测试
&ifEquipment= mobile  //手机端（mobile：手机端； wap:手机网站；web:pc端）
"""

import urllib.parse
import requests
import json

import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
    rec=gi.record_by_name(tgt)
    city=rec['city']
    region=rec['region_code']
    country=rec['country_name']
    long=rec['longitude']
    lat=rec['latitude']
    return str(city)
    # print('[+] Target: ' +tgt + ' Geo-located.')
    # print('[+]'+str(city)+', '+str(region)+', '+str(country))
    # print('[+] Latitude: '+str(lat)+', Longitude: '+str(long))
# tat = '116.5.10.8'
# printRecord(tat)

def get_ip_info(ip):
            try:
                headers={'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
                url='https://freeapi.ipip.net/%s' %ip
                r = requests.get(url=url,headers=headers)
                # print(url)
                # print(r)              
                addr=r.text
                # addr2=r.json()
                # addr=json.load(addr)
                return (addr.split('","')[1])
            except:
                    return ("未知")

with open('test.log','r',encoding='utf-8') as f:
    data=[i. strip() for i in f.readlines()]
with open('savedb.txt','a+',encoding='utf-8') as savedb:
    for i in data:
        # print(i)
        my_url = urllib.parse.urlparse(i.split('	')[1])
        # print(my_url)
        query=my_url.query
        # print(query)
        info=urllib.parse.parse_qs(query)
        # print(info)
        try:
            actionBegin=info['actionBegin'][0]
            actionEnd=info['actionEnd'][0]
            actionType=info['actionType'][0]
            actionName=info['actionName'][0]
            actionValue=info['actionValue'][0]
            userUIP=info['userUIP'][0].split('\\')[0]
            actionTest=info['actionTest'][0]
            ifEquipment=info['ifEquipment'][0]
            # 获取ip地址
            addr=printRecord(userUIP)
            # 停留时间
            stayTime=(int(actionEnd)-int(actionBegin))//60
            print(stayTime,actionBegin,actionEnd,actionType,actionName,actionValue,userUIP,actionTest,ifEquipment,addr)
            savedb.write(str(stayTime)+'\t'+actionBegin+' \t'+actionEnd+'\t'+actionType+'\t'+actionName+'\t'+actionValue+'\t'+userUIP+'\t'+actionTest+'\t'+ifEquipment+'\t'+addr+'\n')
        except:
            print('fail')


    
    