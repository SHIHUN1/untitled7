from Common.http_requests import HttpRequests
import json
import logging
from Common import logger
from Test_data import CommonData
import pytest



TICKETNO={}
@pytest.mark.smoke
@pytest.mark.usefixtures("refund_consent_dara2")
class Testrefundconsent:
    @pytest.mark.parametrize("item",CommonData.test_data2)
    def test_refund(self,refund_consent_dara2,item):
        res = HttpRequests().http_requests(item['URL'], json.dumps(eval(item['Param'])), item['Method'],
                                           eval(item['headers']))
        try:
            assert item['ExpectedResult'] == res.json()['code']
            TestResult = 'PASS'
        except AssertionError as e :
            logging.error('请求出错了:{0}'.format(e))
            TestResult = 'FAIL'
            raise
        finally:
             refund_consent_dara2.write_back(item['CaseId'] + 1, 8, str(res.json()))
             refund_consent_dara2.write_back(item['CaseId'] + 1, 9, TestResult)

    @pytest.mark.parametrize("item",CommonData.test_data)
    def test_refund_pass(self,refund_consent_dara1,item):
        global TICKETNO
        if item['Param'].find('${ticketNo}') != -1:
               new_param = item['Param'].replace('${ticketNo}', str(TICKETNO))

        else:
            new_param = item['Param']
        res = HttpRequests().http_requests(item['URL'], json.dumps(eval(new_param)), item['Method'],
                                           eval(item['headers']))
        if item['URL'].find('apply') != -1:
            if res.json()['data'].get('ticketNo'):
                TICKETNO = res.json()['data'].get('ticketNo')


        try:
            assert item['ExpectedResult']==res.json()['code']
            TestResult = 'PASS'
        except AssertionError as e:
            logging.error('请求出错了:{0}'.format(e))
            TestResult = 'FAIL'
            raise e

        finally:
            refund_consent_dara1.write_back(item['CaseId'] + 1, 8, str(res.json()))
            refund_consent_dara1.write_back(item['CaseId'] + 1, 9, TestResult)

