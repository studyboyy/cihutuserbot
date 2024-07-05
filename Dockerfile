FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \
    libavformat-dev \
    libavutil-dev \
    libswscale-dev \
    libavresample-dev \
    build-essential \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*
    
# Clone repository and set permissions
RUN git clone -b main https://github.com/studyboyy/cihutuserbot.git /home/Kazuuserbot/ \
    && chmod -R 777 /home/Kazuuserbot \
    && mkdir /home/Kazuuserbot/bin/

# Copy configuration files
COPY ./sample_config.env ./config.env* /home/Kazuuserbot/

# Set working directory
WORKDIR /home/Kazuuserbot/

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install requirements
RUN pip install -r requirements.txt

# Start the application
CMD ["bash", "start"]
