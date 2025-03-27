# FROM node:22.14-alpine

# RUN npm install -g lighthouse
# WORKDIR /app
# COPY run-lighthouse.js .
# CMD ["node", "run-lighthouse.js"]

FROM node:22.14-slim

# Install system dependencies for Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    libglib2.0-0 \
    libnss3 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Install Lighthouse and chrome-launcher globally (opcional, já que estão no package.json)
RUN npm install -g lighthouse chrome-launcher

# Ensure NODE_PATH is set correctly
ENV NODE_PATH=/usr/local/lib/node_modules

# Set Chromium path explicitly
ENV CHROME_PATH=/usr/bin/chromium

# Copy the script
COPY run-lighthouse.js .

# Ensure permissions for Chromium
RUN chmod -R o+rwx /usr/local/lib/node_modules /usr/bin/chromium

CMD ["node", "run-lighthouse.js"]