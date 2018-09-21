FROM dhpcontainreg.azurecr.io/core-image/python:3.6
RUN git clone https://github.com/dhpgitub/ms-name-normalization.git
WORKDIR /ms-name-normalization
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
# set env var ZipkinURL=http://localhost:9411/api/v1/spans and app_name=ms-name-normalization
CMD ["app.py"]
