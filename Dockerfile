FROM python:3

COPY entrypoint.py /

RUN pip install sh

EXPOSE 3306

ENTRYPOINT "python" "entrypoint.py"
