FROM python:3.6
WORKDIR /motonowblog
ADD . /motonowblog
RUN pip install -r requirements.txt