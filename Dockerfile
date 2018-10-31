FROM python:3.6-alpine3.6

WORKDIR /flaskeleton

COPY . /flaskeleton

RUN pip install pipenv && pipenv install

EXPOSE 5005

ENV NAME flaskeleton

CMD ["pipenv", "run", "python", "server.py", "-p", "prod", "--db-init"]