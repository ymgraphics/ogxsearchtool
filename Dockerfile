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
ENV API_TOKEN=1837525814:AAEGfFv1rSm0EegY1M_xnxEAbf1UD-cv6eo
ENV API_KEY=09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9

# Run the bot
CMD [ "python", "main.py" ]
