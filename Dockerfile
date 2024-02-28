FROM python:3.10-alpine
COPY ./requirements.txt /app/requirements.txt
COPY . .
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["python3"]
CMD ["app.py"]

