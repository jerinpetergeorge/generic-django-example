FROM python:3.9

LABEL maintainer="Jerin Peter George <jerin.peter@kuwaitnet.com>"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY ./ /app/

# Install dependencies
RUN pip install pip -U && pip install -r requirements.txt
