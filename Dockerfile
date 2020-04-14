FROM python:alpine
COPY app.py /usr/src/myapp/app.py
WORKDIR /usr/src/myapp/
CMD ["1","2","3"]
ENTRYPOINT ["python3","app.py"]