# FastAPI NER Service

This project deploys a transformer-based Named Entity Recognition (NER) model using FastAPI. It processes financial news content to extract stock symbols and associated data. The service is containerized with Docker and can be run using Docker Compose for easy management.

## Prerequisites

- Python 3.9+ (if not using Docker)
- Docker
- Docker Compose

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mrkhedri/initial-news-classification-with-fastapi.git
cd initial-news-classification-with-fastapi
```

### 2. Set Up the Environment
Ensure that the .env file is in the root of your project and contains the necessary environment variables for your configuration.

### 3. Install Dependencies
Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application Using Uvicorn
After installing the dependencies, you can run the FastAPI application using uvicorn. Use the following command:

```bash
uvicorn app.main:app --reload
```
This will start the FastAPI app locally, and you can access it at:

```arduino
http://localhost:8000
```


## Running the Service with Docker Compose
1. **Docker Compose Configuration:** The `docker-compose.yml` file defines the FastAPI service and environment variables.

2. **Build and Start the Containers:**

```bash
docker-compose up --build
```

3. **Access the FastAPI Service:**

Once the containers are up, you can access the FastAPI application at:

```arduino
http://localhost:8000
```

### Tagging Docker Images
Images are tagged using the format fastapi-ner-service:<DateKey>.<version>. For example:

- First build of the day (April 23, 2025):

```bash
docker build -t fastapi-ner-service:20250423.01 .
```

- Second build of the same day:

```bash
docker build -t fastapi-ner-service:20250423.02 .
```

