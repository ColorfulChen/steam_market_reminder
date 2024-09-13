# steam_market_reminder
每日通过Github Actions和serverchan给我的微信发送iflow.watch上分析的挂刀行情。

在github action中设置serverchan的sendkey即可使用。sendkey获取地址：[SendKey (ftqq.com)](https://sct.ftqq.com/sendkey)

# How to Use
1. Fork this repository
2. subcribe serverchan(方糖) on wechat.
3. apply for serverchan sendkey. see[SendKey (ftqq.com)](https://sct.ftqq.com/sendkey).
4. go to your forked reposiroty page.
5. go to settings->Secrets and Varibles->New repository secret->set "SERVERCHANSENDKEY" to your sendkey you just applyed in step 3.