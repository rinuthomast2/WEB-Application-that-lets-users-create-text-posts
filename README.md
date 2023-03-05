# WEB-Application-that-lets-users-create-text-posts
WEB Application that lets users create text posts.  On top of the page, add a text field that allows the user to search for ALL posts.
Project Description
This project is a web application that allows users to create and search for text posts. It uses a React frontend with Material UI and a Python backend with SQLAlchemy to store post data in a PostgreSQL database. Search results are cached using SOLR for faster search performance. The project is designed according to the Onion Architecture and includes unit tests for all APIs.

Why
The purpose of this project is to demonstrate proficiency in several technologies commonly used in web development, including React, Material UI, Python, SQLAlchemy, PostgreSQL, SOLR, and Docker. By creating a web application with these technologies, I aim to showcase my ability to design, develop, and deploy a full-stack application using a modern tech stack.

How
The web application consists of a single-page app built with React, which communicates with a Python backend over a REST API. The backend uses SQLAlchemy to store and retrieve post data in a PostgreSQL database. To speed up search queries, search results are cached using SOLR. The application is designed according to the Onion Architecture, with domain-specific business logic at the core of the system, surrounded by application-specific and infrastructure-specific layers.

To deploy the application, Docker and docker-compose are used to create containers for the frontend, backend, PostgreSQL database, and SOLR cache. The containers are orchestrated using docker-compose to allow for easy deployment and management of the application.

What
The web application allows users to create and search for text posts. Upon opening the application, the user is prompted to enter their name before being shown the main page. On the main page, the user can create a new post by entering their message and clicking the "Create Post" button. The post includes the user's name, message, and a timestamp indicating when the post was created.

The user can also search for posts using the search bar at the top of the page. As the user types, the application will display a message indicating that a search is happening. If search results are found, they will replace the current content on the page. If there are no posts to show, the application will display a message encouraging the user to create a post. If the search returns no results, the application will display a message indicating that the search phrase returned no results.
