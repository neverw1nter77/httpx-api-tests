# HTTPX API Tests

This project contains automated API tests for the public Swagger Petstore API.  
The tests are written using **Python**, **Pytest**, **HTTPX**, **Pydantic**, **Allure** and **Faker**.

The goal of this project is to show practical experience in building a clean and scalable API test framework, using approaches similar to real QA automation projects.

## Project Overview

The test suite focuses on validating core API functionality such as:

- creating, updating and deleting entities
- verifying API responses and status codes
- validating response schemas
- working with different request types (GET, POST, PUT, DELETE)

The project is built with an emphasis on readability and maintainability.  
Key parts of the architecture include:

- API clients for working with endpoints
- Pydantic schemas for request/response validation
- Pytest fixtures for reusable setup
- Fake data generation for dynamic test data
- Allure reports for test result visualization

The structure is designed to be simple but scalable, so new endpoints and tests can be added easily.

## Allure Report

You can view the latest test report here:  
https://neverw1nter77.github.io/httpx-api-tests/

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/neverw1nter77/httpx-api-tests.git
cd httpx-api-tests