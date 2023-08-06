# syntax=docker/dockerfile:1

# start by pulling the python image
FROM python:3.8-slim-buster

LABEL maintainer="Raben Shrestha <xraben5@gmail.com>"

# switch working directory
WORKDIR /app

# ADD . /app

# copy the requirements file into the image
COPY requirements.txt requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

EXPOSE 5000

# configure the container to run in an executed manner
CMD ["python3", "app.py"]