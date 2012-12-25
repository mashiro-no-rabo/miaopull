Miaopull ｢喵噗哦｣
=====

Intro
-----
Miaopull is an auto-pull util upon Flask.

She can watch multiple repos on Github or Bitbucket, automatically pull the newest code on the watching branch, build or deploy with your custom commands, and send emails to your team once everything works fine.

｢簡介｣
-----
｢喵噗哦｣是由Flask驅動的自動代碼更新工具.

她可以監視來自Github或Bitbucket的多個代碼庫, 自動下載指定分支上的最新代碼並執行自定義命令來構建或部署你的代碼, 最後發郵件通知你的團隊.

Setup
-----

1. clone the repo to your server
2. change `miao.json` accrodingly
3. make a `virtualenv` and activate it
4. `pip install -r requirements.txt`
5. `python miao.py &`
6. setup hooks and add your url
   - Github: `Settings` > `Service Hooks` > `WebHook URLs`
   - Bitbucket: `admin` > `Services` > `POST`

｢安裝｣
-----

1. 下載代碼至服務器
2. 根據需要修改配置文件`miao.json`
3. 創建虛擬環境並激活(推薦使用`virtualenv`, 否則`pip`指令可能需要`root`權限)
4. 同上
5. 同上
6. 配置鉤子(具體方法同上)

About `miao.json`
-----

```
{
    "port": 8088, # on which port miaopull runs
    "email_notify": false, # true to enable sending email
    "email_settings": {
    # safe to ignore these if not sending email
        "host": "smtp.gmail.com",
        "port": 465,
        "mode": "ssl",
        "login": "your_account@example.com",
        "password": "your_gmail_password",
        "sender_name": "｢喵｣",
        "sender_email": "someone@example.com",
        "default_recipients": [
        # if no specified recipients use these
            "someone@example.com",
            "someone_else@example.com"
        ]
    },
    "repos": [
        {
            "path": "/Users/aquarhead/Projects/miaopull",
            "branch": "master",
            "commands": [
            # custom commands to execute after pull
            # working dir is "path"
                "mv settings_server.py settings.py",
                "mv consts_server.py consts.py"
            ],
            "specify_recipients": [
                "someone@example.com"
            ]
        }
    ]
}
```

｢配置 `miao.json`｣
-----

```
{
    "port": 8088, # 喵運行的端口
    "email_notify": false, # 設置爲true來啓用郵件通知
    "email_settings": {
    # 若未啓用郵件通知可以忽略
        "host": "smtp.gmail.com",
        "port": 465,
        "mode": "ssl",
        "login": "your_account@example.com",
        "password": "your_gmail_password",
        "sender_name": "｢喵｣",
        "sender_email": "someone@example.com",
        "default_recipients": [
        # 若repo沒有設置收件人則用下列默認
            "someone@example.com",
            "someone_else@example.com"
        ]
    },
    "repos": [
        {
            "path": "/Users/aquarhead/Projects/miaopull",
            "branch": "master",
            "commands": [
            # pull後需要執行的命令, 工作目錄同上面設置的"path"
                "mv settings_server.py settings.py",
                "mv consts_server.py consts.py"
            ],
            "specify_recipients": [
                "someone@example.com"
            ]
        }
    ]
}
```