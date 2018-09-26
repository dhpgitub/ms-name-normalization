FROM dhpcontainreg.azurecr.io/core-image/python:3.6 as build
RUN git clone https://github.com/dhpgitub/ms-name-normalization.git
WORKDIR /ms-name-normalization
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv ms-name-normalization
RUN du
RUN pip install -r requirements.txt
FROM dhpcontainreg.azurecr.io/core-image/python:3.7-alpine3.7
WORKDIR /ms-name-normalization
COPY --from=build /ms-name-normalization /ms-name-normalization
ENTRYPOINT ["python"]
# set env var ZipkinURL=http://localhost:9411/api/v1/spans and app_name=ms-name-normalization
CMD ["app.py"] 
