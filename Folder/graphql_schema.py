import strawberry
from typing import List
from app.database import SessionLocal
from app.models import Branch as BranchModel, Bank as BankModel

# Define the GraphQL Bank type
@strawberry.type
class Bank:
    name: str

# Define the GraphQL Branch type
@strawberry.type
class Branch:
    ifsc: str
    branch: str
    bank: Bank

# Define the GraphQL Query
@strawberry.type
class Query:
    @strawberry.field
    def branches(self) -> List[Branch]:
        db = SessionLocal()
        branch_models = db.query(BranchModel).all()
        result = [
            Branch(
                ifsc=b.ifsc,
                branch=b.branch,
                bank=Bank(name=b.bank.name)
            )
            for b in branch_models
        ]
        db.close()
        return result

# Create the GraphQL schema
schema = strawberry.Schema(query=Query)
