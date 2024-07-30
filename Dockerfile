# We are using an official Python runtime as a parent image
FROM python:3.9-slim

# We are setting up the working directory in the container
WORKDIR /app

# We are Copying just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# We are Installing  any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# We are Copying the rest of the application
COPY . /app

# The Command to run on container start is 
CMD ["python", "main.py"]
