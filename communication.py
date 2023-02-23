"""
Contain the communication between the client and
"""

import requests
import consts


def send_snippet(snippet, **kwargs):
    print(snippet)
    response = requests.request(consts.HTTP_METHOD, consts.url, data={consts.HTTP_VARIABLE: snippet},
                                headers={},
                                **kwargs)
    print(response.text)
    answer = response.text.split(consts.RESPONSE_SEPARATOR)[1].split(consts.INNER_SEPERATOR)
    return answer
