# Simple Flask Application

This is a simple Flask application that serves as an example of building a REST API with Swagger documentation. The application includes endpoints that read from dictionaries and also interfaces with external APIs. It provides functionality to retrieve Kevin's favorites based on a specified topic and fetches a random joke from the JokeAPI.

## Requirements

- Python 3.x
- Flask
- Flask-RESTx
- requests

## Installation

1. Clone the repository:

  ```bash
    git clone https://github.com/kgaban/simple-flask-app.git
  ```
    
2.  Navigate to the project directory:
    
    
  ```bash
    cd simple-flask-app
  ```
    
3.  Create a virtual environment (optional but recommended):
        
  ```bash
    python -m venv
  ```
    
4.  Activate the virtual environment:
    
  ```bash
    source venv/bin/activate   # On macOS/Linux

    venv\Scripts\activate      # On Windows
  ```
    
5.  Install the required dependencies:
    
  ```bash
  pip install -r requirements.txt
  ```
    

## Usage

Run the Flask application:

```bash
  python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Endpoints

### 1\. Hello World

*   **Endpoint**: `/hello`
    
*   **Method**: GET
    
*   **Description**: Simple hello world GET request.
    
*   **Example Response**:
    
  ```json
    {"message": "World!"}
  ```
    

### 2\. Kevin's Favorites

*   **Endpoint**: `/favorites`
    
*   **Method**: GET
    
*   **Parameters**:
    
    *   `topic` (string, required): Topic to find Kevin's favorite.
*   **Description**: Takes a topic and returns Kevin's favorite for that topic.
    
*   **Example Response**:
    
    
  ```json
  {"message": "Kevin's Favorite color is 'blue'!"}
  ```
    

### 3\. Random Joke

*   **Endpoint**: `/joke`
    
*   **Method**: GET
    
*   **Description**: Fetches a random joke from the JokeAPI.
    
*   **Example Response**: (The actual response will vary as it's a random joke)
    
    ```bash
    "Why don't scientists trust atoms? Because they make up everything!"
    ```