# ForgetMe

ForgetMe is an innovative project designed to empower users to take control of their online privacy. This tool connects to users' SMTP servers, identifies the services that sent them emails, and sends GDPR data removal requests to those domains.

## Features

* Connects to users' SMTP servers
* Identifies services that sent emails
* Retrieves privacy or iod emails from those domains
* Automatically generates GDPR data removal requests
* User-friendly web interface for selecting domains to act upon

## Goals

* Enhance online privacy for individuals
* Simplify the process of requesting data removal under GDPR regulations
* Provide a user-friendly interface for managing domain-specific requests

## Installation

### Option 1: Standard Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ForgetMe.git
   cd ForgetMe
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the provided `.env.example`:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your own settings.

### Option 2: Docker Installation (Recommended)

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ForgetMe.git
   cd ForgetMe
   ```

2. Create a `.env` file based on the provided `.env.example`:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your own settings.

3. Build and run the Docker container:
   ```
   docker-compose up -d
   ```

## Usage

### If using standard installation:

1. Start the application:
   ```
   python main.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

### If using Docker:

1. The application should already be running after `docker-compose up -d`

2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

3. Follow the on-screen instructions to:
   - Connect to your email account
   - View services that have your data
   - Select which services to send GDPR requests to
   - Send and monitor your GDPR data removal requests

## Docker Commands

- Start the application:
  ```
  docker-compose up -d
  ```

- View logs:
  ```
  docker-compose logs -f
  ```

- Stop the application:
  ```
  docker-compose down
  ```

- Rebuild the application after changes:
  ```
  docker-compose build
  docker-compose up -d
  ```

## Implementation Details

This application is built with:
- Python 3.8+
- FastAPI for the backend framework
- Jinja2 templates for server-side rendering
- Modern HTML5, CSS3, and JavaScript for the frontend
- Docker for containerization and easy deployment

## Security Considerations

This application is designed with security in mind:
- Email credentials are used only for the scanning process and are never stored
- All connections are made securely
- No personal data is retained longer than necessary

## Contributing

Contributions are welcome! If you're interested in helping with development, please open an issue or submit a pull request.
