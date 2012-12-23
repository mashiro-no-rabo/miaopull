Miaopull ｢喵噗哦｣
=====

Intro
-----
Miaopull is an auto-pull util upon Flask.

She can watch multiple branches of multiple repos, if any of these changed she will pull the newest code from Github or Bitbucket automatically.

｢簡介｣
-----
｢喵噗哦｣是由Flask驅動的自動代碼更新工具.

她可以監視多個代碼庫的多個分支, 若其中任一有更新即會自動下載, 支持Github和Bitbucket.

Setup
-----

1. clone the repo to your server
2. change `miao.json` accrodingly
3. make a virtualenv and activate it
4. `pip install -r requirements.txt`
5. `python miao.py &`
6. setup hooks and add your url
   - Github: `Settings` > `Service Hooks` > `WebHook URLs`
   - Bitbucket: `admin` > `Services` > `POST`

｢配置｣
-----

1. 下載代碼至服務器
2. 根據需要修改配置文件`miao.json`
3. 創建`virtualenv`並激活
4. 同上
5. 同上
6. 配置鉤子(具體方法同上)