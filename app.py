import click
import psutil

from lib.location_history_driver import LocationHistoryDriver


@click.command()
@click.option("--headless", default=True)
@click.option("--user-data-dir", required=True)
@click.option("--profile-directory", required=True)
def app(headless, user_data_dir, profile_directory):
    # 既にChromeが動いていると動かないので、殺す
    for p in psutil.process_iter():
        try:
            if p.name() == "chrome.exe":
                p.terminate()
        except Exception as ex:
            print(ex)
            pass

    # ロケーション履歴をエクスポートする
    driver = LocationHistoryDriver(
        headless=headless,
        user_data_dir=user_data_dir,
        profile_directory=profile_directory,
    )
    driver.download()


app()
