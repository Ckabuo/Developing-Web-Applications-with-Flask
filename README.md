# Building a Full-Stack Web App with Flask

## Overview

This repository contains the project files and documentation for the "Building a Full-Stack Web App with Flask" quest from StackUp's "Developing Web Applications with Flask" campaign. This quest guides you through creating a full-stack web application using Flask, a micro web framework for Python, covering both frontend and backend development.

## Learning Outcomes

By the end of this quest, you will be able to:
- Set up a Flask application with a connected database.
- Implement RESTful API endpoints in Flask.
- Build a responsive frontend using HTML, CSS, and JavaScript.
- Integrate frontend and backend to create a full-stack web application.

## Quest Details

### Introduction
This quest focuses on building a complete web application with Flask, encompassing both server-side and client-side development. You will learn how to create and manage routes, handle forms, interact with a database, and serve static files.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Basic knowledge of Python, HTML, CSS, and JavaScript.
- Familiarity with Flask framework.

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Ckabuo/Developing-Web-Applications-with-Flask.git
    cd Developing-Web-Applications-with-Flask
    git checkout -b main3
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory and add your configuration variables:
    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

### Running the Application

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to see the application in action.

## Project Structure

```plaintext
full-stack-flask-app/
│
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
├── templates/          # HTML templates
│   └── ...
├── static/             # Static files (CSS, JS, images)
│   └── ...
├── models.py           # Database models
├── routes.py           # Application routes
└── README.md           # Project documentation
