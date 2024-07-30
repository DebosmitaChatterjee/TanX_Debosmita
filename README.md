# My Project

## Description
This project is designed to analyze customer orders from an online store, providing detailed reports on revenues by month, product, and customer. The goal is to empower business decision-making with actionable insights that are derived from a given historical data.

## Project Structure
Below is the directory and file structure of the project that I have executed :

```plaintext
my_project/
│
├── MAIN
│   ├── main.py               # Main Python script with data analysis logic
│
├── tests/
│   ├── test.py          # Tests for the data analysis functions
│
├── db/
│   ├── init.sql              # SQL scripts for database setup
│
├── .dockerignore             # Specifies files to ignore in Docker builds
├── Dockerfile                # Defines the Docker environment for the app
├── docker-compose.yml        # Manages container orchestration for development
├── requirements.txt          # Lists dependencies for the project
└── README.md                 # Describes the project
```


## Architecture Overview
The application is structured as follows:
- Back-end framework: Here the Python scripts perform data processing and analytics.
- Database: PostgreSQL is used for storing order data securely and in an efficient manner.
- Caching: Here Redis is implemented to enhance the performance of repeated queries.
- Additional services: This Includes services like logging and monitoring for better maintenance and operation.

## Technologies Used
- Python
- Pandas for data manipulation
- Pytest for testing
- Docker for containerization
- PostgreSQL as the relational database
- Redis for caching

### The necessary Prerequisites
Before running the project, we have to ensure that we have Docker and Docker Compose installed which are essential tools for creating and managing our application's containers.

### Installing and Running with Docker

#### 1. Building the Docker Image
To build the Docker image which contains our application and its environment, we have to run in the terminal:

docker build -t myproject-image 

 ### 2. Running the Application using Docker Compose
To start all services in the docker-compose.yml file, we need to execute:

docker-compose up --build

### 3. Running Tests
We need to run tests to ensure the application behaves as required and expected :

docker-compose run --rm app pytest

### Accessing the Application
After we run the docker-compose up command, the application should be accessible and giving results in the terminal or via  web browser through the URL , typically http://localhost:PORT where PORT is the port number configured for the web service in our docker-compose.yml.



