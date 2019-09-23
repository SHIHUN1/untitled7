from Common.doexcel import DoExcel
from Common import read_path


test_data=DoExcel(read_path.excel_path, 'test_data1').do_excel()
test_data2=DoExcel(read_path.excel_path, 'test_data2').do_excel()