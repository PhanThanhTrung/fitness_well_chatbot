FROM python:3.10.14-bullseye

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs
WORKDIR /app

COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "bash" ]
# ENTRYPOINT [ "sleep infinity" ]
