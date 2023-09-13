# Django REST API Documentation

## Overview

This documentation provides information on how to use the Django REST API for managing "Person" records. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records.

## Table of Contents

1. [Setup](#setup)
2. [API Endpoints](#api-endpoints)
   - [Create a Person](#create-a-person)
   - [Fetch Details of a Person](#fetch-details-of-a-person)
   - [Update a Person](#update-a-person)
   - [Delete a Person](#delete-a-person)
3. [Request/Response Formats](#request-response-formats)
4. [Sample Usage](#sample-usage)
5. [Known Limitations](#known-limitations)

## Setup

To use the Django REST API, follow these setup instructions:

1. Clone the repository from GitHub:

   ```bash
   git clone <repository_url>
   cd <repository_directory>

   1. Create a virtual environment and activate it

     ```bash
     python -m venv venv
     source venv/bin/activate



## Know Limitations
- The API does not support batch operations.
- Authentication and authorization mechanisms are not implemented in this sample.
- Input validation checks for string fields only; other data types are not allowed.
- Duplicate name validation is performed only during creation, not during updates.