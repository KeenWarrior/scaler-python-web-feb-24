from unittest import mock
from api_logic import get_current_time

import requests


@mock.patch("requests.get")
def test_get_current_time(mocked_get):
    mocked_response = mock.Mock()
    mocked_response.status_code = 201

    expected_time = "2024-02-24T20:42:08.496066+05:30"
    mocked_response.json.return_value = {
        "datetime": "2024-02-24T20:42:08.496066+05:30"
    }

    mocked_get.return_value = mocked_response
    result = get_current_time()

    assert result == expected_time

