# SQLAlchemy
#### **By Kelvin Kipchumba **
This project demonstrates the use of SQLAlchemy with Alembic for database migrations and includes a set of CRUD operations with associated tests.

## Getting Started
These instructions will help you set up and run the project on your local machine.

### Prerequisites
Make sure you have Python and Pipenv installed on your machine.
   - Commands used earlier - Remember I already created migrations and models
        - ```pipenv install alembic``` => Installs Alembic package for database migrations
        - ```alembic init alembic``` => Initializes Alembic, creates the necessary configuration files and directories 
        - ```alembic revision --autogenerate -m "initial"``` => Generates an automatic migration script with a message "initial" - after which you add your code for perfoming operations on your db
        - ```alembic upgrade head``` - Applies the generated migration script to update the database to the latest version 
        - Now this mean i have the database with tables.


## Setup/Installation Requirements
    - Download a file in the code section to the desired folder
    - Extract the files
    - Open the folder with vs code.
    - Activate the virtual environment in the terminal using ```pipenv shell``` command them ```pipenv install```
   
## Folder Structure
├── lib
│   ├── config.py     Contains configurations and common imports for seed and main files
│   ├── main.py       Main CRUD operations file for Posts and Users
│   ├── seed.py       Seed script for initial data
│   └── models.py     SQLAlchemy models file
├── tests.py           Example usage of methods from main.py
├── alembic
│   ├── versions      Alembic migration versions
├── Tests.py          Example usage of methods in lib/main.py
├── alembic.ini        Alembic configuration file

  - The rest are most common files

  So after all that run
  - ```python lib/seed.py``` to add initial data to posts and users tables 
  - ```python Tests.py``` to run example tests
  - And all is done

### License
*Licenced under the MIT licence
Free of use
