# Base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV BOT_TOKEN=1837525814:AAEGfFv1rSm0EegY1M_xnxEAbf1UD-cv6eo

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY main.py .

# Expose the port that the bot listens on
EXPOSE 8443

# Run the bot
CMD ["python", "main.py"]
