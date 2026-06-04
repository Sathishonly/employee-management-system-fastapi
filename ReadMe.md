# Employee Management System

## Overview

Employee Management System built using FastAPI, PostgreSQL, SQLAlchemy, Alembic, and JWT Authentication.

## Features

* User Registration
* User Login
* JWT Authentication
* Refresh Token
* Protected APIs
* Employee Create
* Employee Update
* Employee Delete
* Employee List
* Pagination
* Search by Name and Email
* Joining Date Filters
* PostgreSQL Database
* Alembic Migrations

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT
* Argon2 Password Hashing

## API Endpoints

### Authentication

POST /registeruser

POST /login

POST /refreshtoken

### Employees

POST /createemployee

GET /getemployeelist

GET /getemployee/{employeeId}

PUT /editemployee/{employeeId}

DELETE /deleteemployee/{employeeId}

## Installation

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
