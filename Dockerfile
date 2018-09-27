FROM dhpcontainreg.azurecr.io/core-image/python:3.6-alpine3.8
RUN apk add --no-cache --virtual .build-deps bash git openssh && \
    git clone https://github.com/dhpgitub/ms-name-normalization.git && \
    apk del .build-deps
WORKDIR /ms-name-normalization
RUN apk add --no-cache --virtual .build-deps build-base && \
    pip install --no-cache-dir  -r requirements.txt && \
    apk del .build-deps
USER 1000
ENTRYPOINT ["python3"]
# set env var ZipkinURL=http://localhost:9411/api/v1/spans and app_name=ms-name-normalization
CMD ["app.py"]
