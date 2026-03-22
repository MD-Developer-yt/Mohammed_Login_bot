# ========================================================
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
# ========================================================

FROM python:3.10.13-slim-bullseye

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure logs are shown instantly
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start ONLY the bot
# Flask keep_alive server handles port binding
CMD ["python3", "bot.py"]

# ========================================================
#Don't Remove Credits 
#Supports Group @AU_Bot_Discussion 
#Telegram Channel @Anime_UpdatesAU
#Developer @Mr_Mohammed_29
# ========================================================
