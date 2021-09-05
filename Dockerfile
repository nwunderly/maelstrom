FROM python:3.8-slim
WORKDIR /johnmallard
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "main.py"]