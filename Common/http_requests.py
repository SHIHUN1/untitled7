import requests
import logging
from Common import logger

class HttpRequests():
    def http_requests(self,url,param,method,headers):
        if method=='get':
            try:
                res=requests.get(url,param,headers=headers,verify=False)
            except Exception as e:
                logging.error('get请求出错了{0}'.format(e))
                raise e
        elif method=='post':
            try:
                res=requests.post(url,param,headers=headers,verify=False)
            except Exception as e:
                logging.error('post请求出错了{0}'.format(e))
                raise e
        elif method=='put':
            try:
                res=requests.put(url,param,headers=headers,verify=False)
            except Exception as e:
                logging.error('put请求出错了{0}'.format(e))
                raise e
        else:
            logging.info('接口请求出错了')
        return res
