FROM nginx

RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 도 가질 수 있으니 유의!
# 도커 파일이 위치한 곳 기준이므로 수정해준다. (/home/alt 니까 )
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

# 업데이트 및 ssh 설치
RUN  apt-get -yq update && \
     apt-get -yqq install ssh

# github에 등록해둔 SSH key를 옮겨줘서, 묻는 과정 없애게 한다
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN echo "test21"

WORKDIR /home/alt

RUN mkdir ./build
# ubunut 에 있는 build 파일을 해당 파일로 alt로 ./build로 옮겨준다
ADD ./build/web ./build

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]