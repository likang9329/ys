import csv
import os

import requests
from requests import Session
import configparser as cp


class Base:
    #获取环境
    def getUrl(self):
        config=cp.ConfigParser()
        root_dir = os.path.dirname(os.path.abspath('.'))
        if root_dir.split('\\')[-1]=='ys':
            path=root_dir+'\conf\config.ini'
            config.read(path,encoding='GB18030')
            return config.get('hj','url')
        else:
            path=root_dir+'\ys\conf\config.ini'
            config.read(path, encoding='GB18030')

        # config.read(r'C:\Users\Administrator\PycharmProjects\yhzx\conf\config.ini',encoding='GB18030 ')
            return config.get('hj','url')
        # f = '..\conf\config.ini'
        # inifile = cp.ConfigParser()
        # inifile.read(f, 'utf8')
        #
        # return inifile.get('hj', 'url')

    # def read_inis(self):
    #     parent_dir = os.path.dirname(os.path.abspath(__file__))
    #     conf = configparser.ConfigParser()
    #     conf.read(os.path.join(parent_dir, 'E:/pythonProject/xiangmu3/configss/inst'), encoding="utf-8")
    #     return conf



    def send_request(self,method,url,params=None,data=None,json=None,**kwargs):

        if method in ('p','post'):
            res = requests.post(url,data=data,json=json,**kwargs)
        elif method in ('g','get'):
            res = requests.get(url,params=params,**kwargs)
        else:
            raise Exception('暂不支持其他请求方法')
        return res

    def session(self):
        return Session()

class CsvHelp:
    def get_csv_data(self,filePath,mode='r',encoding='utf8'):
        data_list = []
        file = open(filePath,mode=mode,encoding=encoding)
        csv_data = csv.reader(file)
        for i in csv_data:
            data_list.append(tuple(i))
        file.close()
        return data_list

if __name__ == '__main__':
    l=Base().getUrl()
    print(l)
