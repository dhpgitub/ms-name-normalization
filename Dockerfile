FROM dhpcontainreg.azurecr.io/dhpcore/python:3.7-alpine3.7
RUN apt-get update
RUN apt-get install gcc
WORKDIR /code
ADD . /code
RUN ls -alFrt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "-Xapp_name=ms-name-normalization", "-XZipkinURL=http://localhost:9411/api/v1/spans", "app.py"]