from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)
current_value = 0
# max_value = 100

def update_counter():
    global current_value
    while True:
    # while current_value < max_value:
        current_value += 1
        time.sleep(1)

@app.route('/')
def get_current_value():
    return jsonify({'current_value': current_value})

if __name__ == '__main__':
    threading.Thread(target=update_counter).start()
    app.run(host='0.0.0.0',port=8080)