# Bank-API


This project implements a GraphQL API for retrieving information about Indian banks and their branches. It uses **FastAPI**, **Strawberry GraphQL**, and a pre-filled **SQLite database** (`data.db`). The goal is to provide an efficient, scalable backend that supports querying relational data using modern Python tools.

---

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
🛠Local Development Setup
1. Set up Virtual Environment
bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the API Server
bash
Copy
Edit
uvicorn app.main:app --reload
