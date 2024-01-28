

# Base stage for production
#FROM arm32v7/python:3.8-alpine as base
#RUN apk update
#RUN apk add python3-dev

FROM arm32v6/python:3.8-alpine as base
RUN apk update && apk add python3-dev

WORKDIR /app
ENV FLASK_APP=flaskr

COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt
COPY . .


# Test stage for testing
FROM base as test
COPY requirements/test.txt .
RUN pip install --no-cache-dir -r test.txt
COPY tests/ /app/tests/

RUN ["flake8", "flaskr/"]
RUN ["flake8", "tests/"]

RUN ["coverage", "run", "-m", "pytest", "-m", "unit"]
RUN ["coverage", "run", "-m", "pytest", "-m", "api"]
RUN ["coverage", "report", "--fail-under", "80"]

#RUN ["pytest", "-m", "unit"]
#RUN ["pytest", "-m", "api"]

FROM base as prod

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

