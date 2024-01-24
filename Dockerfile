

# Base stage for production
FROM python:3.8-slim as base
WORKDIR /app
COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt
COPY . .


# Test stage for testing
FROM base as test
COPY requirements/test.txt .
RUN pip install --no-cache-dir -r test.txt
RUN ["pytest"]

FROM base as prod

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

