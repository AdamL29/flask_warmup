from flask import Flask
from dbhelpers import run_statement
import json

app = Flask(__name__)

@app.get('/api/books')
def get_books():
    result = run_statement("CALL all_books")
    if (type(result) == list):
        result_json = json.dumps(result)
        return result_json
        # Short term is = return json.dumps(result)
    else:
        return "Sorry, something went wrong."

@app.get('/api/books_authored')
def get_books_authored():
    result = run_statement("CALL book_count")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong."

@app.get("/api/best_selling_book")
def get_best_selling_book():
    result = run_statement("CALL most_copies")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong."

@app.get("/api/best_selling_author")
def get_best_selling_author():
    result = run_statement("CALL successful_authors")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong."

app.run(debug = True)