# CVE Management Application

This project is a simple Flask-based web application that allows you to add and view Common Vulnerabilities and Exposures (CVEs) from a MongoDB database. The app provides two main endpoints:

- **POST /cves**: Add a new CVE to the database.
- **GET /seecves**: Retrieve a list of all CVEs stored in the database.

The app uses Flask for the web framework and MongoDB as the database to store the CVEs. The data is serialized and displayed in a formatted way for easy viewing.
 the tools I’ve used in this task : 
 1. Flask :  used to create a simple API that interacts with MongoDB. It defines two routes: one to add CVEs (/cves) and another to retrieve them (/seecves).
 2. MongoDB :  used in this project to store CVEs. The application connects to MongoDB via PyMongo, a Python driver for MongoDB, allowing the app to insert and retrieve CVEs stored as documents.
 3. PyMongo : used to connect the Flask application to MongoDB.
 4. Requests : used in the test.py script to send POST requests to the Flask API to add CVEs to the MongoDB database. It also sends GET requests to retrieve the stored CVEs.
    
