# Retrying downloads
import requests


def Download(url, num_retries=2):
    print("Downloading: ", url)
    headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/80.0.3987.149 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("Downloading error: ", e)
        response = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                return Download(url, num_retries - 1)

    return response


# html = Download(url=URL)
# print(html.text)
