from flask import Flask, render_template, jsonify
import time
import threading
import os

app = Flask(__name__)

NUMBER_FILE = './data/number.txt'  # Path where the number is stored

# Function to load the number from the file, or initialize with 0
def load_number():
    try:
        with open(NUMBER_FILE, 'r') as f:
            return int(f.read().strip())  # Remove potential whitespace
    except (FileNotFoundError, ValueError):  # Handle missing file or invalid data
        return 0

# Function to save the number to the file
def save_number(number):
    os.makedirs(os.path.dirname(NUMBER_FILE), exist_ok=True)  # Create data directory if needed
    with open(NUMBER_FILE, 'w') as f:
        f.write(str(number))

# Function to continuously increment and save the number
def increment_and_save():
    global number
    while True:
        number += 1
        save_number(number)
        time.sleep(1)

# Initialize the number on application startup 
number = load_number()

# Start the increment_number function in a background thread
thread = threading.Thread(target=increment_and_save)
thread.daemon = True
thread.start()


# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to fetch the current number
@app.route('/get_number')
def get_number():
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=False)
