ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-slim AS baseworkdir

WORKDIR /app

COPY app/ /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

ENV FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0"]
