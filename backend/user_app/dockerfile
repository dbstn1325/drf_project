FROM python:3.9.1

RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 도 가질 수 있으니 유의!
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

# github에 등록해둔 SSH key를 옮겨줘서, 묻는 과정 없애게 한다
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/alt/

RUN echo "test21"

# release/0.1 branch 로부터 깃 클론을 진행해준당
RUN git clone -b release/0.3 --single-branch git@github.com:alt-comapny/AllLeaveTrip.git

WORKDIR /home/alt/AllLeaveTrip/backend

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000"]