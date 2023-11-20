FROM python:3.9-alpine
COPY ./requirements.txt /app/
WORKDIR /app
RUN set -eux; \
    pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD ["main.py" ]