FROM python:3.7

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 9999
CMD ["python"]