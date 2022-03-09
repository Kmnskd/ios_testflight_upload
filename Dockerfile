FROM python:3.8

COPY src /usr/local/ios_testflight/srv

WORKDIR /usr/local/ios_testflight/srv

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]