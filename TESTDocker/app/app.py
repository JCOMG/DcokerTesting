from flask import Flask

app = Flask(__name__)


@app.route('/')

@app.route('/health')
def index():
    return "okkkkkkk!!!!!!!!!"

def test_index():
    assert True



if __name__ == '__main__':
    app.run(debug=True, port=5000)
