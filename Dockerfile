FROM python:3.10-slim

# Set the working directory
ENV APP_HOME /app
WORKDIR ${APP_HOME}

# Copy contents of current folder into the working directory
COPY . .

# Install necessary packages and dependencies
RUN apt-get update && apt-get install -y build-essential gcc sudo curl && \
    pip install -r requirements.txt

# Install ngrok
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
    sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
    sudo tee /etc/apt/sources.list.d/ngrok.list && \
    sudo apt update && sudo apt install -y ngrok

# Load NGROK_TOKEN from the .env file
RUN export $(cat .env | xargs) && \
    ngrok config add-authtoken $NGROK_TOKEN && \
    rm -rf .env

# Execute commands to run the api
CMD bash -c "ngrok http --domain=bat-absolute-apparently.ngrok-free.app 12000 & \
    uvicorn api:app --host 0.0.0.0 --port 12000"
