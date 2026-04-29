FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flet
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8550
CMD ["python", "app.py"]