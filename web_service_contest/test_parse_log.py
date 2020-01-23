from web_service_contest.parse_log import parse_log

from unittest.mock import patch

@patch("requests.models.Response.text")
def test_parse_log(requests_get_mock):
    requests_get_mock.return_value = """/wiki,2019-00-01 00:00:00.000000\n
                                        /wiki,2019-00-01 00:00:00.000000,0:00:07.544390,200\n
                                        /api_wiki,2019-00-01 00:00:00.000000\n
                                        /api_wiki,2019-00-01 00:00:00.000000,0:00:07.544390,200\n
                                     """

    print(parse_log(""))
    assert 2 == parse_log("")
