import unittest
from Common.http_requests import HttpRequests
from Common.doexcel import DoExcel
from Common import read_path
from ddt import ddt,data
import json
import logging
from Common import logger




test_data=DoExcel(read_path.excel_path, 'test_data1').do_excel()
test_data2=DoExcel(read_path.excel_path, 'test_data2').do_excel()
TICKETNO={}

@ddt
class TestRes(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel(read_path.excel_path, 'test_data1')
    @data(*test_data)
    def test_http(self,item):
        global TICKETNO
        if item['Param'].find('${ticketNo}') != -1:
            new_param = item['Param'].replace('${ticketNo}', str(TICKETNO))
        else:
            new_param = item['Param']
        res=HttpRequests().http_requests(item['URL'],json.dumps(eval(new_param)),item['Method'],eval(item['headers']))

        if item['URL'].find('apply') :
            if res.json()['data'].get('ticketNo'):
                TICKETNO=res.json()['data'].get('ticketNo')

        try:
            self.assertEqual(item['ExpectedResult'],res.json()['code'])
            TestResult='PASS'
        except Exception as e :
            logging.error('请求出错了:{0}'.format(e))
            TestResult='FAIL'
            raise e
        finally:
            self.t.write_back(item['CaseId']+1,8,str(res.json()))
            self.t.write_back(item['CaseId']+1,9,TestResult)

@ddt
class TestTicket(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel(read_path.excel_path, 'test_data2')

    @data(*test_data2)
    def test_ticket(self,item):
        res = HttpRequests().http_requests(item['URL'], json.dumps(eval(item['Param'])), item['Method'],eval(item['headers']))
        try:
            self.assertEqual(item['ExpectedResult'],res.json()['code'])
            TestResult='PASS'
        except Exception as e :
            logging.error('请求出错了:{0}'.format(e))
            TestResult='FAIL'
            raise e
        finally:
            self.t.write_back(item['CaseId']+1,8,str(res.json()))
            self.t.write_back(item['CaseId']+1,9,TestResult)
