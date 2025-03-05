# ATS (Applicant Tracking System)

## Overview

The **Applicant Tracking System (ATS)** is a Django-based web application designed to manage candidate data efficiently. It provides API endpoints to perform CRUD operations on candidate records and supports a powerful search feature that ranks candidates based on relevance.

---

## Features

### 1. **Candidate Management**

- Add new candidates.
- Retrieve a list of all candidates.
- Update candidate details.
- Delete candidates.

### 2. **Advanced Search**

- Search candidates by name.
- Results are ranked based on exact matches and partial word matches.
- Higher relevance is given to full matches.
- Implements dynamic filtering using Django ORM expressions.

### 3. **Relevancy-Based Sorting**

- Candidates are ranked by **search term match count**.
- Full-name exact matches appear **at the top**.
- Partial matches are ordered based on the number of matched words.

### 4. **Exception Handling & Logging**
- Implemented robust exception handling to ensure API stability.
- Added logging to track application behavior and errors.
- Logs are stored in a structured format for debugging and monitoring.

### 5. **Environment Variables Support**
- Configurations such as database credentials and API keys are managed using .env files.
- Ensures security by keeping sensitive information outside the codebase.

---

## API Endpoints

### **1. Candidate Endpoints**

| Method | Endpoint            | Description              |
| ------ | ------------------- | ------------------------ |
| GET    | `/ATS/candidates/`      | List all candidates      |
| POST   | `/ATS/candidates/`      | Create a new candidate   |
| GET    | `/ATS/candidates/{id}/` | Retrieve candidate by ID |
| PUT    | `/ATS/candidates/{id}/` | Update candidate details |
| DELETE | `/ATS/candidates/{id}/` | Delete a candidate       |

### **2. Search Endpoint**

| Method | Endpoint                       | Description               |
| ------ | ------------------------------ | ------------------------- |
| GET    | `/ATS/candidates/search?q={query}` | Search candidates by name |

**Example:**

```
GET /ATS/candidates/search?q=Raj Sharma
```

**Response:** Candidates sorted by search relevance.

---

**Postman Collection:** [Click here](https://drive.google.com/file/d/1vS7bmUZMVjrbXo90QQQH00jqWFZ-XrVs/view?usp=sharing)

---

## Installation & Setup on local system (ubuntu)

- Clone git repo
        - git clone https://github.com/GautmSahu/ATSProject.git
    - Create virtual environment(python=3.11)
        - python3 -m venv venv
    - Activate the environment
        - . venv/bin/activate
    - Go to project path
        - cd ATSProject/
    - Install required packages
        - pip install -r requirements.txt
    - Setup postgres and create database
        - open postgres shell and paste below cmds
            - CREATE DATABASE db_name; 
            - CREATE USER db_user WITH PASSWORD 'secure_password';
            - ALTER ROLE db_user SET client_encoding TO 'utf8'; 
            - ALTER ROLE db_user SET default_transaction_isolation TO 'read committed'; 
            - ALTER ROLE db_user SET timezone TO 'UTC'; 
            - GRANT ALL PRIVILEGES ON DATABASE db_name TO db_user; 
    - Open .env file and do the necessary changes like DB configuration etc.
    - Export the environment variables
        - source .env
    - Run migrations
        - python manage.py makemigrations
        - python manage.py migrate
    - Run the django server
        - python manage.py runserver
        - Check the api's with the help of postman collection providedd above
    - That's it.

---

## Technologies Used

- **Django Rest Framework (DRF)** - For building APIs
- **PostgreSQL** - Database
- **Django ORM** - Query management

---

## Future Enhancements

- Implement authentication & user roles.
- Add pagination for candidate listings.
- Improve search accuracy using Full-Text Search (FTS).

---

## Thank you! 😊



