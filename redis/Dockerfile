FROM toastyboii/base-ol9:v0.0.1
ARG REDIS_USER=redis
ARG REDIS_USER_HOME=/home/redis
ARG REDIS_CUSTOM_PORT=9736
ARG REDIS_CONF_DIR_PATH=/etc/redis
ARG REDIS_WORKING_DIR_PATH=/var/redis
ARG REDIS_LOG_DIR_PATH=/var/log
ARG REDIS_PID_DIR_PATH=/run
COPY user.sh /tmp
RUN sh /tmp/user.sh $REDIS_USER
USER $REDIS_USER
WORKDIR $REDIS_USER_HOME
COPY install.sh $REDIS_USER_HOME
RUN sh install.sh
COPY systemd-redis_server.service $REDIS_USER_HOME
COPY redis.conf $REDIS_USER_HOME
COPY install-more-properly.sh $REDIS_USER_HOME
RUN sh install-more-properly.sh $REDIS_USER $REDIS_CUSTOM_PORT $REDIS_CONF_DIR_PATH $REDIS_WORKING_DIR_PATH $REDIS_LOG_DIR_PATH $REDIS_PID_DIR_PATH
ENV REDIS_CONF_PATH="/etc/redis/${REDIS_USER}_${REDIS_CUSTOM_PORT}.conf"
EXPOSE $REDIS_CUSTOM_PORT
ENTRYPOINT redis-server $REDIS_CONF_PATH --requirepass p422w0rd






