# google-location-history-exporter

Googleロケーション履歴を、Google Driveにエクスポートするツール (Seleniumを使用)

## 前提

- 既にGoogleにログイン済みのChromeのプロファイルを使うこと
- 既にGoogleのパスワードを保存済みのChromeのプロファイルを使うこと
- Windowsで動かす前提(他OSで動くかは未確認)
- pyenv-win (https://github.com/pyenv-win/pyenv-win)


## 導入

```
> 00_setup.bat
```


## 使用

```
> python -m pipenv run python app.py ^
    --headless False ^
    --user-data-dir "C:\Users\XXXXXX\AppData\Local\Google\Chrome\User Data" ^
    --profile-directory "Profile 1"
```

Google Driveの、マイドライブ → Takeoutフォルダ に格納されます

