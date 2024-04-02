# Use the official Python base image
FROM python:3.10.13-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Rust toolchain to build pydantic which is a dependency of fastapi
# Install build dependencies for C extensions
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libffi-dev rustc cargo \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages using pip
RUN pip install fastapi pylint black isort uvicorn

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
