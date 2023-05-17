#!/bin/bash
#Author: Nicolas Nunez

USER=${1}
echo "Creating user ${USER} to run Redis and all related..."
HOME_DIRECTORY=/home/${USER}
useradd \
--create-home \
--home-dir ${HOME_DIRECTORY} \
--comment "User to run Redis services" \
--shell /bin/bash \
--uid 1000 \
--user-group \
${USER}

echo "Just in case..."
chown -R ${USER}:${USER} ${HOME_DIRECTORY}
ls -lrt ${HOME_DIRECTORY}/..

SUDOERS=/etc/sudoers.d/${USER}
text="%${USER}        ALL=(ALL)       NOPASSWD: ALL"
echo ${text}
cat <<EOF >>${SUDOERS}
${text}
EOF

chmod 0440 ${SUDOERS}
