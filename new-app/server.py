from flask import Flask, render_template, jsonify
import time
from threading import Thread

app = Flask(__name__)

# Global variable to store the number
number = 0

# Function to continuously increment the number
def increment_number():
    global number
    while True:
        number += 1
        time.sleep(1)

# Start the increment_number function in a separate thread
thread = Thread(target=increment_number)
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
    app.run(debug=True)
