# Bank-API


This project implements a GraphQL API for retrieving information about Indian banks and their branches. It uses **FastAPI**, **Strawberry GraphQL**, and a pre-filled **SQLite database** (`data.db`). The goal is to provide an efficient, scalable backend that supports querying relational data using modern Python tools.

---
🧠 Methodology / Approach
Problem
Create an API service to retrieve data about Indian banks and their branches, using either REST or GraphQL. Bonus points for clean code, test cases, and deployment (e.g., on Heroku).

✅ Solution Strategy
1. Choosing the Stack
Framework: I chose FastAPI due to its modern async capabilities, simplicity, and native GraphQL support through libraries like Strawberry.
Database: Used SQLite with a prefilled data.db file for easy portability and demo purposes.
GraphQL: Selected Strawberry GraphQL to expose a single endpoint (/gql) that can fetch nested bank and branch data in a single query.
ORM: Used SQLAlchemy to define models and handle database operations.

🛠 Step-by-Step Implementation
1.Project Setup
  Initialized a Python virtual environment and created a clean modular structure under app/.
  
2. Database Design
  Created two tables: banks and branches.
  Populated them using the prefilled data.db file.

3.Modeling with SQLAlchemy
  Defined Bank and Branch models in models.py.
  Setup relationships using ForeignKey and relationship.

4.GraphQL Schema Design
  Created BankType and BranchType in graphql_schema.py.
  Wrote a query branches that returns all branch records along with nested bank names.

5.GraphQL Integration
  Mounted the GraphQL schema using Strawberry at /gql.

6.Testing
  Manually tested the API using GraphQL Playground at /gql.
  Wrote a basic test in test_app.py using FastAPI’s TestClient.


 Why GraphQL?
Allows fetching deeply nested related data (e.g., a branch and its associated bank) in a single call.
Flexible querying improves front-end performance by avoiding over-fetching or under-fetching.

Sample Query Used
graphql
Copy code
query {
  branches {
    ifsc
    branch
    bank {
      name
    }
  }
}
 Time Taken
Task	Duration
Planning & Setup	2 hour
Coding (Backend + Models)	3 hours
GraphQL & Testing	3 hour
Deployment & README	1 hour
Total	~9 hrs

##  Features

- GraphQL endpoint at `/gql`
- Fetch all branches with nested bank information
- SQLite-based lightweight database
- Clean modular code
-Includes sample query and instructions

---

##  Tech Stack

- Python 3.10+
- FastAPI
- Strawberry GraphQL
- SQLAlchemy ORM
- SQLite (for demo)
- Uvicorn (ASGI server)


---

##  Project Structure

Folder file contain all the necessary codes and requirements file in it. They have be structed like:

bank_api/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── graphql_schema.py
├── data.db
├── requirements.txt
├── runtime.txt
├── .gitignore
├── README.md
---
## Sample GraphQL Query

You can run the following query at `/gql`:

```graphql
query {
  branches {
    ifsc
    branch
    bank {
      name
    }
  }
}
---
🛠Local Development Setup
1. Set up Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
3. Run the API Server
uvicorn app.main:app --reload
