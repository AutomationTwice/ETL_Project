# README

## Overview
This ETL (Extract, Transform, Load) project is designed to automate the process of extracting data from CSV files, transforming it as needed, and loading it into a PostgreSQL database. The project leverages Docker for containerization, ensuring a consistent and reproducible environment for running the ETL processes. Additionally, Visual Studio Code is used as the primary development environment, with PostgreSQL serving as the database management system. Python, along with several essential libraries, is utilized to handle data extraction, transformation, and loading.

### Features
- Data Extraction: Automatically reads data from CSV files located in the specified directory.
- Data Transformation: Includes options to transform data, such as renaming columns, filtering records, and applying data transformations.
- Data Loading: Efficiently loads the transformed data into a PostgreSQL database.
- Containerization: Uses Docker to create isolated environments, simplifying dependency management and deployment.
- Database Management: Adminer is included as a lightweight web-based database management tool for PostgreSQL, accessible via a web browser.

### Technologies Used
- Docker: For creating and managing containers.
- Visual Studio Code: As the Integrated Development Environment (IDE) for developing and running the project.
- PostgreSQL: Database system used to store and manage the data.
- Python: Programming language used for scripting the ETL process, including libraries like pandas and sqlalchemy.
### Use Cases
- Data Integration: Combine data from multiple CSV files into a single, coherent database.
- Data Cleaning: Transform raw data into a clean, usable format for analysis or reporting.
- Automated Workflows: Schedule the ETL process to run at specific intervals, ensuring up-to-date data without manual intervention.
- Future Enhancements
- Support for Additional Data Sources: Extend the project to extract data from APIs, databases, or other file formats.
- Advanced Transformations: Implement more complex data transformations, such as aggregations, data enrichment, and validation.
- Scalability: Optimize the ETL process to handle larger datasets and improve performance.
- Monitoring and Logging: Add monitoring and logging capabilities to track the ETL process and diagnose issues.

### Getting Started
Follow the setup instructions below to get the project up and running on your local machine.



### Prerequisites
List all software dependencies and tools required to run your ETL project. Include links to where each can be obtained.
- Docker
- Visual Studio Code
- PostgreSQL database
- Python 3.x
- Required Python packages (list them with pip install -r requirements.txt)

### Setup Instructions
1. Clone Repository:
```
https://github.com/AutomationTwice/ETL_Project.git
```
2. Start Docker Containers:
```
docker-compose up -d
```
This command starts the PostgreSQL database and Adminer (optional for database management).

3. Create Python Virtual Environment (Optional but recommended):

```
python -m venv venv
. venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. Install Python Dependencies:

```
pip install -r requirements.txt
```
### Project Structure
Describe the structure of your project directory. Explain where to find important files, such as:

- etl.py: Main ETL script
- docker-compose.yml: Docker configuration
- data/: Directory for storing input data
- README.md: Documentation file (this file)

### Running the ETL Process
1. Prepare Input Data:
   Place your CSV file(s) in the data/ directory.

2. Run the ETL Script:

```
python etl.py
```
   This script extracts data from CSV, transforms it (optional), and loads it into PostgreSQL.

### Database Management
### - Accessing Adminer:
Open a web browser and go to http://localhost:8080. Use the PostgreSQL login details to manage your database via Adminer.

### Additional Notes
- Virtual Environment: It's recommended to use a Python virtual environment to manage dependencies. This can prevent conflicts between project-specific packages and globally installed packages.
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Data Directory: Ensure your CSV files are placed in the data/ directory. This directory is configured in the etl.py script.

- Database Configuration: The database configuration is specified in the docker-compose.yml file. You can change the PostgreSQL user, password, and database name as needed.

- Adminer Usage: Adminer is a web-based database management tool included in the project. You can access it at http://localhost:8080 to manage your PostgreSQL database.

- Regular Backups: It's a good practice to regularly back up your PostgreSQL database to prevent data loss.

### Troubleshooting
- Docker Containers Not Starting:

   - Ensure Docker is installed and running on your machine.
   - Check if the ports 5432 (PostgreSQL) and 8080 (Adminer) are available and not being used by other services.
   - Use the command docker-compose logs to view the logs and diagnose the issue.

- Database Connection Errors:

   - Verify that the PostgreSQL container is running using docker ps.
   - Ensure the database configuration (username, password, database name) in etl.py matches the configuration in docker-compose.yml.

- Python Dependency Issues:

   - Ensure all required Python packages are installed by running pip install -r requirements.txt.
   - If using a virtual environment, make sure it is activated.

- CSV File Path Issues:

   - Verify that the CSV file path specified in etl.py is correct.
   - Ensure that the CSV file exists in the data/ directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


