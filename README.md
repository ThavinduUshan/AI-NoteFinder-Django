# NoteFinder: AI-Powered Note Retrieval Application

## Overview

NoteFinder is a Django-based application designed to assist users in efficiently retrieving relevant notes based on specific concepts or keywords. Often, individuals take numerous notes on various topics, making it challenging to locate specific information later. NoteFinder aims to alleviate this issue by leveraging the power of artificial intelligence (AI) and the OpenAI API, specifically utilizing the Retrieval Augmented Generation (RAG) approach.

## Features

- **Note Management**: Users can create, edit, and organize their notes within the application.
- **AI-Powered Search**: NoteFinder employs the RAG approach to intelligently retrieve relevant notes based on user queries.
- **Vector Database Integration**: ChromaDB is utilized as the vector database to efficiently store and retrieve note vectors.

## Endpoints

### Notes

- **GET /notes/**
  - Retrieves a list of all notes along with their categories.
  
- **POST /notes/**
  - Creates a new note.
  - Request body should contain JSON data with note details.
  - Upon successful creation, the note is added to the database and indexed for search.

### Search

- **GET /notes/search/**
  - Searches for notes based on a provided query.
  - Query parameter:
    - `query`: The search query to find relevant notes.
  - Returns up to 6 most relevant notes based on the query.

### Categories

- **GET /notes/categories/**
  - Retrieves a list of all available categories.
  
- **POST /notes/categories/**
  - Creates a new category.
  - Request body should contain JSON data with category details.
  - Upon successful creation, the new category is added to the database.


## Technologies Used

- **Django**: Python-based web framework for rapid development of web applications.
- **OpenAI API**: Provides access to powerful AI models for natural language processing tasks.
- **ChromaDB**: Vector database optimized for similarity search and efficient storage of high-dimensional data.
- **PostgreSQL**: Relational database management system used for data storage.

## Getting Started

To get started with NoteFinder, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your Django environment and configure database settings.
4. Obtain API keys for OpenAI API and configure them in the application settings.
5. Initialize ChromaDB and configure it for use with NoteFinder.
6. Run the Django development server using `python manage.py runserver`.

## Contributions

Contributions to NoteFinder are welcome! If you have any suggestions, bug reports, or would like to contribute code, feel free to open an issue or submit a pull request.
