FROM python:3.10.5

EXPOSE 8000
WORKDIR /designhub

ADD requirements.txt /designhub
    
RUN pip install -r requirements.txt

ADD ./designhub /designhub

CMD gunicorn    --bind 0.0.0.0:8000      \
                --reload designhub.wsgi:application