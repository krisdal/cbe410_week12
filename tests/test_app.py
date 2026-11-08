from app import app

def test_health():
    with app.test_client() as client:
        assert client.get('/health').json == {'status': 'ok'}

def test_greet_limit():
    with app.test_client() as client:
        assert client.get('/greet?name=' + 'a'*60).json['message'] == 'Hello, ' + 'a'*40 + '!'

def test_calculate():
    with app.test_client() as client:
        response = client.get('/calculate?expression=5*3.2')
        assert response.get_data() == b'16.0'
