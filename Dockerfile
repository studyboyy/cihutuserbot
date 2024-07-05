FROM python:3.10
RUN git clone -b main https://github.com/studyboyy/cihutuserbot.git /home/Kazuuserbot/ \
    && chmod -R 777 /home/Kazuuserbot \
    && mkdir /home/Kazuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Kazuuserbot/

WORKDIR /home/Kazuuserbot/

RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["bash","start"]
