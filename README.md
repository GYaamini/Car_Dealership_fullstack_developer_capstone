# Car Dealership Web Application

## Overview
This repository contains the full-stack implementation for the Car Dealership website. The application integrates multiple services, including a backend built with **Express.js** and **MongoDB**, a **Sentiment Analyzer microservice** deployed on **IBM Code Engine**, and a frontend developed using **HTML, CSS, and JavaScript**. The Django application is used to handle core functionalities, including managing car models and makes.

## Prerequisites

Before proceeding, ensure the following services are set up and running:

1. **Car Dealership Website**: 
   - The website should be fully functional and meet the specified requirements.
   - Make sure you’ve completed the lab to create the Car Dealership website.

2. **Sentiment Analyzer Service**:
   - The Sentiment Analyzer microservice should be deployed on **IBM Code Engine** and accessible.
   - Follow the steps in the lab *Deploy Sentiment Analysis on Code Engine as a Microservice*.

3. **Backend Service (Express + MongoDB)**:
   - Ensure the backend with **Express.js** and **MongoDB** is running.
   - Follow the lab *Implement API Endpoints using Express-Mongo* to set up the backend.

4. **Frontend (Client-Side)**:
   - The client-side should be built and ready for integration.
   - Follow the lab *Build the Client-Side and Configure it in the Lab User Management*.

5. **Django (Main Application) Server**:
   - The Django application server should be running.
   - Follow the section *Environment Setup in the Lab Build CarModel and CarMake Django Models* to configure the Django application.


## Installation

### 1. Clone the Repository

- git clone https://github.com/your-username/Car_Dealership_fullstack_developer_capstone.git
- cd Car_Dealership_fullstack_developer_capstone


### 2. Backend Setup
Ensure you have Node.js and MongoDB installed, then run the backend service.

**Build docker image and run docker-compose**:

    - cd server/database
    - docker build . -t nodeapp
    - docker-compose up

    - cd server/carInventory
    - docker build . -t nodeapp
    - docker-compose up

### 3. Sentiment Analyzer Service Setup
Make sure the sentiment analyzer microservice is deployed on IBM Code Engine and is accessible at a valid URL or have valid Docker image

**Build microservice**:

    - docker built . -t <namespace>/senti_analyzer
    - docker push <namespace>/senti_analyzer

**Run application**:

    - ibmcloud ce application create --name setimentanalyzer --image <namespace>/senti_analyzer --registry-secret --icr-secret --port 5000

**Example curl command to test if the Sentiment Analyzer service is working**:

    - curl https://your-sentiment-analyzer-url.com/analyze?text=your_text_here


### 4. Frontend Setup
Ensure the frontend is properly configured and can be served either with a simple web server or via integration with the backend.

**Install frontend dependencies**:

    - cd server/frontend
    - npm install

**Build frontend**:

    - npm run build


### 5. Django Application Setup
Make sure the Django server is running and the necessary migrations for CarModel and CarMake have been applied.

**Install Django dependencies**:

    - cd server
    - pip install virtualenv
    - virtualenv djangoenv
    - source djangoenv/bin/activate

    - pip install -r requirements.txt

**Run Django migrations**:

    - python manage.py makemigrations
    - python manage.py migrate

**Start the Django server**:

    - python manage.py runserver


## Configured ports
1. Django application - 8000
2. Backend for Dealership - 3030
3. Backend for Car Inventory - 3050
4. Sentiment Analyzer microservice - 5000


# Acknowledgments
Thanks to the IBM instructors for providing resources related to this web application development.
