FROM python:3.10.5

RUN mkdir -p /usr/src/robobet
WORKDIR /usr/src/robobet

RUN pip install --upgrade pip

COPY . /usr/src/robobet
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3","main.py"]