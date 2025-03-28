from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a request model
class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}

@app.post("/query")
def process_query(request: QueryRequest):
    # Simulate converting a natural language query to pseudo-SQL
    if "sales" in request.query.lower():
        pseudo_sql = "SELECT * FROM sales_data WHERE condition='some condition';"
    elif "users" in request.query.lower():
        pseudo_sql = "SELECT * FROM user_data WHERE condition='some condition';"
    else:
        pseudo_sql = "SELECT * FROM unknown_table WHERE condition='some condition';"
    
    return {"pseudo_sql": pseudo_sql}

@app.post("/explain")
def explain_query(request: QueryRequest):
    # Simulating an explanation of the query
    explanation = f"Your query is about: '{request.query}'. It looks for relevant data."
    return {"explanation": explanation}

@app.post("/validate")
def validate_query(request: QueryRequest):
    # Basic validation: Check if query contains "SELECT"
    if "select" in request.query.lower():
        return {"valid": True, "message": "Query is valid SQL-like."}
    else:
        return {"valid": False, "message": "Query does not follow SQL-like format."}
