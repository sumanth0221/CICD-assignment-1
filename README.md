# CICD-assignment

This repository is a sample Python project designed to demonstrate the implementation of Continuous Integration and Continuous Delivery (CI/CD) pipelines. It is intended as an assignment for exploring automated testing, build processes, and deployment strategies.


## Project Structure

- **.**: Contains the Flask API backend.
- **.github/workflows/**: GitHub Actions configuration files for CI/CD.
- **docker-compose.yml**: Orchestrates the dockerfile

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

Clone the repository and change into the project directory:

```bash
git clone https://github.com/hpcclab/CICD-assignment
cd CICD-assignment
```
## Running the Application

Build and start the services with Docker Compose:

(simple)

```bash
python .\app.py
```

Using Docker - 

```bash
docker-compose up --build
```

### By Default

- The **React frontend** will be available at [http://localhost:3000](http://localhost:3000)
- The **Flask backend API** will run at [http://localhost:5000](http://localhost:5000)

### CI/CD

This repository is set up with GitHub Actions to automatically run tests and build Docker images on commits and pull requests. The CI/CD configuration can be found in the `.github/workflows` directory.
Updated by Sumanth

