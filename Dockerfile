FROM python:3.10.5

EXPOSE 8000
WORKDIR /pine_studio

ADD requirements.txt /pine_studio

RUN pip install -r requirements.txt

ADD ./pine_studio /pine_studio

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--reload", "pine_studio.wsgi:application"]