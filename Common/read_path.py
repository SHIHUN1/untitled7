import os



pro_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


excel_path=os.path.join(pro_path,'Common','BaoJun_Api_case.xlsx')

logs_path=os.path.join(pro_path,"Logs")

baogao_path=os.path  .join(pro_path,'Test_report','baogao.html')