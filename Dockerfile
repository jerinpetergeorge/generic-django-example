# Pull base image
FROM python:3.9 as base
LABEL maintainer="Jerin Peter George <jerinpetergeorge@gmail.com>"

ARG CONTAINER_PORT=5001

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install pip dependencies
RUN pip install pip -U && pip install --no-cache-dir -r requirements.txt -U

# Start APP
CMD bash app-init.sh
