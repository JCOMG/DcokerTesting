ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-slim as baseWORKDIR
COPY TESTDocker/app /app
COPY TESTDocker/app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 5000
ENV FLASK_APP=test_app.py
CMD ["flask", "run", "--host=0.0.0.0"]
