FROM python:3

COPY recipebook /recipebook

WORKDIR /recipebook

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /recipebook/entrypoint.sh

ENTRYPOINT [ "/recipebook/entrypoint.sh" ]
