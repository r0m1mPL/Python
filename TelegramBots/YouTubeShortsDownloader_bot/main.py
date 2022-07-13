from bot import start_telegram_bot
from exeptions import CantDownloadYouTubeVideo


def main():
    try:
        start_telegram_bot()
    except (KeyboardInterrupt, CantDownloadYouTubeVideo,) as error:
        print(error)


if __name__ == "__main__":
    main()
