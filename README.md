# CVE Management Application

This project is a simple Flask-based web application that allows you to add and view Common Vulnerabilities and Exposures (CVEs) from a MongoDB database. The app provides two main endpoints:

- **POST /cves**: Add a new CVE to the database.
- **GET /seecves**: Retrieve a list of all CVEs stored in the database.

The app uses Flask for the web framework and MongoDB as the database to store the CVEs. The data is serialized and displayed in a formatted way for easy viewing.
