from flask import Flask

app = Flask(__name__)


@app.route('/')

@app.route('/index')
def index():
    return "okkkkkkk!!!!!!!!!"

def test_index():
    tester = app.test_client()
    response = tester.get('/index')
    assert response.status_code == 200
    assert b"okkkkkkk!!!!!!!!!" in response.data



if __name__ == '__main__':
    app.run(debug=True, port=5000)
