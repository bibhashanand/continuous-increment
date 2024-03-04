from flask import Flask, render_template, jsonify
import time
import threading
import os

app = Flask(__name__)

NUMBER_FILE = './data/number.txt'

def load_number():
    try:
        with open(NUMBER_FILE, 'r') as f:
            return int(f.read().strip()) 
    except (FileNotFoundError, ValueError):
        return 0

def save_number(number):
    os.makedirs(os.path.dirname(NUMBER_FILE), exist_ok=True) 
    with open(NUMBER_FILE, 'w') as f:
        f.write(str(number))

def increment_and_save():
    global number
    while True:
        number += 1
        save_number(number)
        time.sleep(1)

number = load_number()

thread = threading.Thread(target=increment_and_save)
thread.daemon = True
thread.start()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_number')
def get_number():
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=False)
