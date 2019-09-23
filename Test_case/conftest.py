


import pytest
from Test_data import CommonData
from Common.doexcel import DoExcel
from Common import read_path


@pytest.fixture
def refund_consent_dara2():
    t=DoExcel(read_path.excel_path, 'test_data2')
    yield t


@pytest.fixture
def refund_consent_dara1():
    t=DoExcel(read_path.excel_path, 'test_data1')
    yield t