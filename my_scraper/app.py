from flask import Flask, render_template, request
import json
from search import search_food, search_food2

app = Flask(__name__)

# Load the JSON file once for use in search functions
with open('menu_data.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the search term from the form
    search_term = request.form['food']
    selected_dining_halls = request.form.getlist('dining_hall')  # Get all selected dining halls
    
    # Call the search functions from search.py
    exact_results = search_food(search_term)  # Exact search
    partial_results = search_food2(search_term)  # Partial search

    # If 'All' is selected, show all dining halls and skip filtering for 'dining_hall'
    if 'All' in selected_dining_halls:
        # No need to filter for 'All'; just display results from all dining halls
        pass
    else:
        # Filter results to show only the selected dining halls
        exact_results = [res for res in exact_results if res['dining_hall'] in selected_dining_halls]
        partial_results = [res for res in partial_results if res['dining_hall'] in selected_dining_halls]

    return render_template('results.html', 
                           search_term=search_term, 
                           exact_results=exact_results, 
                           partial_results=partial_results,
                           selected_dining_halls=selected_dining_halls)
if __name__ == "__main__":
    app.run(debug=True)
