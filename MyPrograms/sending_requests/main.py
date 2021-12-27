from fake_useragent import UserAgent
import requests, time


def sending_requests(url="https://r0m1mPL.herokuapp.com"):
    try:
        while True:
            headers = {
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
                "User-Agent": UserAgent().random
            }
            if requests.get(url=url, headers=headers).status_code == 200:
                print("[INFO] Request has been sent, waiting 3 minute...")
                time.sleep(180)
            else:
                return "[ERROR] Status code not 200, script has stopped!!!"
    except Exception as error:
        return f"[ERROR] {error}, script has stopped!!!"


if __name__ == '__main__':
    print(sending_requests())
