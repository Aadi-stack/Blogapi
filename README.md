# FastAPI Blogging 


## Overview
A simple blogging RESTful API built using  Python FastAPI, a modern web framework for building APIs with Python. It allows users to create, read, update, and delete blog posts, comment on posts, and like/dislike them. The data is stored in a MongoDB database.


## Key Features
- **CRUD Operations:** Users can perform CRUD operations on blog posts.
- **Comments:** Users can add comments to posts.
- **Likes/Dislikes:** Users can like or dislike posts.
- **MongoDB Integration:** Data is stored in a MongoDB database.
- **RESTful API:** The API follows RESTful principles for easy integration and usage.

## Technologies Used
- Python
- FastAPI
- MongoDB

## Getting Started
To run this project locally, follow these steps:

1. Clone the repository:
    ```
    git clone <repository_url>
    ```

2. Install dependencies:
    ```
    cd 9AI_blog_api
    pip install -r requirements.txt
    ```
3. Start & Connect to the local MongoDB server:
   If you started MongoDB locally, the FastAPI application should connect to it automatically using the default connection settings. You don't need to make any changes.

4. Run the FastAPI server:
    ```
    uvicorn main:app --reload
    ```

5. Open your browser and navigate to `http://localhost:8000` to access the API documentation and test the endpoints.

## API Routes
- **GET /posts/**: Retrieve all posts.
- **GET /posts/{post_id}/**: Retrieve a single post by ID.
- **POST /posts/**: Create a new post.
- **PUT /posts/{post_id}/**: Update an existing post by ID.
- **DELETE /posts/{post_id}/**: Delete a post by ID.
- **POST /posts/{post_id}/comments/**: Create a new comment on a post.
- **POST /posts/{post_id}/like/**: Like a post.
- **POST /posts/{post_id}/dislike/**: Dislike a post.

## Testing the Endpoints
You can test the API endpoints using tools like cURL, Postman, or any HTTP client. Here are some examples:

- **Create a new post:**
    ```
    curl -X POST "http://localhost:8000/posts/" -H "Content-Type: application/json" -d '{"title": "Example Post", "content": "This is an example post", "author": "name"}'
    ```

- **Retrieve all posts:**
    ```
    curl -X GET "http://localhost:8000/posts/"
    ```

- **Retrieve a single post by ID:**
    ```
    curl -X GET "http://localhost:8000/posts/{post_id}"
    ```

- **Create a new comment on a post:**
    ```
    curl -X POST "http://localhost:8000/posts/{post_id}/comments/" -H "Content-Type: application/json" -d '{"content": "This is a comment", "author": "JaneDoe"}'
    ```

- **Like a post:**
    ```
    curl -X POST "http://localhost:8000/posts/{post_id}/like/"
    ```

- **Dislike a post:**
    ```
    curl -X POST "http://localhost:8000/posts/{post_id}/dislike/"
    ```
