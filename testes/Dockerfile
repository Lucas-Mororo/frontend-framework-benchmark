# Use Ubuntu as base image
FROM ubuntu:22.04

# Set noninteractive to avoid prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    firefox \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python script and requirements
COPY requirements.txt .
COPY firefox_test.py .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set display environment variable
ENV DISPLAY=:99

# Command to keep container running
CMD ["tail", "-f", "/dev/null"]