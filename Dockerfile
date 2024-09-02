FROM python:3.10.9-slim

WORKDIR /app

COPY . /app

CMD ["/bin/bash"]