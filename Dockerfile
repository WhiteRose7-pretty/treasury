FROM python:3.8.5

RUN pip install --upgrade pip

COPY ./web_daria/treasury /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

#ENTRYPOINT ["sh", "/entrypoint.sh"]
