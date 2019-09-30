FROM python:3.7.3

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt
CMD ["python", "run2.py"]
