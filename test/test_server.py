from src.server import APP
import json

def test_receive_links():
    client = APP.test_client()
    url = 'http://localhost:8000/crawl'

    mock_request_data = {
        'links': ['https://www.cs.rpi.edu/~goldsd/index.php']
    }

    response = client.post(url, json=mock_request_data)
    assert response.status_code == 200