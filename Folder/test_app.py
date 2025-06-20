from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_graphql_query():
    query = '''
    query {
        branches {
            edges {
                node {
                    ifsc
                    branch
                    bank {
                        name
                    }
                }
            }
        }
    }
    '''
    response = client.post("/gql", json={"query": query})
    assert response.status_code == 200
    assert "data" in response.json()
