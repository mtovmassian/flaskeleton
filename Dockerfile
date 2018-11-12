FROM python:3.6-alpine3.6

WORKDIR /flaskeleton

COPY . /flaskeleton

RUN apk add -U --no-cache gcc build-base linux-headers ca-certificates python3 python3-dev libffi-dev libressl-dev
RUN pip install pipenv
RUN pipenv install

EXPOSE 5005

ENV NAME flaskeleton

CMD ["pipenv", "run", "python", "server.py", "-p", "prod", "--db-init"]