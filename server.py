from flask import Flask, request


app = Flask(__name__)

print(__name__)

@app.route('/', methods=['POST', 'GET'])
def send_data():
    data = "0"
    return data

@app.route('/internal', methods=['POST', 'GET'])
def get_data():
    data = request.get_data()
    
    
    return data

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')