from app import app

def test_home_page():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.data == b'<p>Hello, World</p>'
