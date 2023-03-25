# Base image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port for Telegram webhook
EXPOSE 8443

# Set environment variables
ENV API_TOKEN=your_token_here
ENV API_KEY=your_key_here

# Run the bot
CMD [ "python", "main.py" ]
