# Import necessary Flask modules
from flask import Flask, render_template, jsonify
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure Flask to serve static files from the 'static' directory
app.static_folder = 'static'

# Define the route for the main dashboard page
@app.route('/')
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template for the dashboard.
    """
    return render_template('index.html')

# --- API endpoints to serve JSON data ---
# Define API endpoint for market share data
@app.route('/api/marketShare')
def market_share_data():
    """
    API endpoint for fetching market share data.
    Reads data from marketShare.json and returns it as JSON.
    """
    filepath = os.path.join('data', 'marketShare.json') # Construct file path
    try:
        with open(filepath, 'r') as f: # Open and read the JSON file
            data = f.read()
            return jsonify(eval(data)) # Return JSON data
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Handle file not found error

# Define API endpoint for revenue trends data
@app.route('/api/revenueTrends')
def revenue_trends_data():
    """
    API endpoint for fetching revenue trends data.
    Reads data from revenueTrends.json and returns it as JSON.
    """
    filepath = os.path.join('data', 'revenueTrends.json') # Construct file path
    try:
        with open(filepath, 'r') as f: # Open and read the JSON file
            data = f.read()
            return jsonify(eval(data)) # Return JSON data
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Handle file not found error

# Define API endpoint for market segmentation data
@app.route('/api/marketSegmentation')
def market_segmentation_data():
    """
    API endpoint for fetching market segmentation data.
    Reads data from marketSegmentation.json and returns it as JSON.
    """
    filepath = os.path.join('data', 'marketSegmentation.json') # Construct file path
    try:
        with open(filepath, 'r') as f: # Open and read the JSON file
            data = f.read()
            return jsonify(eval(data)) # Return JSON data
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Handle file not found error

# --- Run the Flask application ---
if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode for development
