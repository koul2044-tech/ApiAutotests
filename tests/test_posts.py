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
    new_id = post_response.json()["id"]
    url = base_url + f"/posts/{new_id}"
    response = requests.get(url)
    assert response.status_code == 200


def test_put(base_url):
    url = base_url + "/posts/1"
    payload = {"title": "Заголовок_новый", "body": "Новый текст", "user_id": 1}
    put_response = requests.put(url, json=payload)
    get_response = requests.get(url)
    assert get_response.status_code == 200
    server_data = get_response.json()
    assert server_data["title"] == "Заголовок_новый"
    assert server_data["body"] == "Новый текст"
