from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'helfdjjsaflo world'

if __name__ == '__main__':
    app.run()