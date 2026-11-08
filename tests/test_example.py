import requests


def test_status_code():
  """Простой тест для проверки доступности публичного API."""
  url = "https://jsonplaceholder.typicode.com/posts/1"
  response = requests.get(url)

  assert response.status_code == 200, (
      f"Ожидался статус 200, но получен {response.status_code}"
  )
  data = response.json()
  assert data["id"] == 1