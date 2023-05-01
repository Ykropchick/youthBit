FROM python:3.11

ENV PYTHONDONTWRITEBYTEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
ENV APPDIR=/app

WORKDIR $APPDIR

RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev
RUN apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN apt-get install -y netcat

COPY requirements_prod.txt $APPDIR
RUN pip install -r requirements_prod.txt

COPY ./entrypoint_web.sh $APPDIR/entrypoint_web.sh
RUN chmod +x $APPDIR/entrypoint_web.sh

COPY . $APPDIR

RUN mkdir "staticfiles"

ENTRYPOINT [ "/app/entrypoint_web.sh" ]