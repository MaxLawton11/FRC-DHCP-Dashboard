from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Path to the JSON file where button selection data will be saved
DATA_FILE = 'selections.json'

# Helper function to read data from the JSON file
def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Helper function to write data to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_selection', methods=['POST'])
def save_selection():
    # Get data from the POST request (button selection)
    data = request.get_json()
    # Save the data to the JSON file
    write_data(data)
    return jsonify({"message": "Data saved successfully!"}), 200

@app.route('/view_selection')
def view_selection():
    # Read the data from the JSON file
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
