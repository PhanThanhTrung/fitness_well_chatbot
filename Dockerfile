FROM python:3.10.14-bullseye
WORKDIR /app

ARG NODE_MAJOR=20

RUN apt-get update \
  && apt-get install -y ca-certificates curl gnupg \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update \
  && apt-get install nodejs -y \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python

COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python3 manage.py tailwind install --no-input;
RUN python3 manage.py tailwind build --no-input;

CMD [ "bash" ]
# ENTRYPOINT [ "sleep infinity" ]
