FROM python:3
ARG APP_NAME="konnector"
WORKDIR /usr/src/app
RUN mkdir $APP_NAME
WORKDIR /usr/src/app/$APP_NAME
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY konnector .
RUN ls -lrt
#CMD [ "python", "app.py" ]
ENTRYPOINT ["sh", "-c", "/bin/bash"]