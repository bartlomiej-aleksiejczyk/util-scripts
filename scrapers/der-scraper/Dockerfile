FROM python:3.9-slim

WORKDIR /usr/src/app

RUN groupadd -r appuser && useradd -r -g appuser -d /usr/src/app -s /sbin/nologin -c "Docker image user" appuser

RUN chown -R appuser:appuser /usr/src/app

COPY --chown=appuser:appuser . .

RUN pip install --no-cache-dir requests beautifulsoup4 boto3

USER appuser

CMD ["python", "./scraper.py"]

