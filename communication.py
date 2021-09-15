"""
Contain the communication between the client and
"""

import requests
import consts


def send_snippet(snippet, **kwargs):
    response = requests.request(consts.HTTP_METHOD, consts.url, data={consts.HTTP_VARIABLE: snippet},
                                headers={},
                                **kwargs)
    answer = response.text.split(consts.SEPARATOR)[1]
    return answer
