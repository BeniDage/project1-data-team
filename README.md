# Project1 Web Server

This project is a web server application that connects to a MongoDB database. The setup uses Docker Compose to manage the services.

## Prerequisites

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/BeniDage/project1-data-team.git

cd Project1

```

### 2. Run Docker Compose to build the images and run the services:

- docker-compose up --build

### 3. View the Application

- Open your browser and navigate to http://localhost:5003/

### Changing MongoDB Documents and Collections

- config.py contains the MongoDB connection string.
- document_model.py contains the MongoDB collection name.
