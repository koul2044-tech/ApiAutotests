import requests


def test_get(base_url):
    url = base_url + "/posts"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_post(base_url):
    url = base_url + "/posts"
    payload = {"title": "Заголовок", "body": "Тело запроса", "user_id": 1}
    post_response = requests.post(url, json=payload)
    assert post_response.status_code == 201
    response_data = post_response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
