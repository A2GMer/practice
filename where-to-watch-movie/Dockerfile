FROM python:3.7
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN mkdir -p /opt/wheretowatch/src
COPY ./src/requirements.txt /opt/wheretowatch/src
WORKDIR /opt/wheretowatch/src
RUN pip install -r requirements.txt

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt update
RUN apt install -y google-chrome-stable
RUN pip install chromedriver-binary==116.0.5845.96.0
# Install ChromeDriver
RUN curl -O https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
WORKDIR /opt/wheretowatch/src
RUN unzip chromedriver_linux64.zip
RUN apt install -y libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev
