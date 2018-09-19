FROM dhpcontainreg.azurecr.io/core-image/python:3.6
WORKDIR /code
ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-Xapp_name=ms-name-normalization", "-XZipkinURL=http://localhost:9411/api/v1/spans", "app.py"]
