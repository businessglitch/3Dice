
class TestPage(object):
    def test_home_page(self, client):
        "Home page should respond with a success 200"
        response = client.get("http://localhost:3000/")
        assert response.status_code == 200

    def test_terms_page(self, client):
        "Terms page should respond with a success 200"
        response = client.get("http://localhost:3000/terms/")
        assert response.status_code == 200

    def test_privacy_page(self, client):
        "Privacy page should respond with a success 200"
        response = client.get("http://localhost:3000/privacy/")
        assert response.status_code == 200