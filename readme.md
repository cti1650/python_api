# python api server run on vercel
To have your account on https://vercel.com/ first.

# 必要なライブラリを取込
```
pip freeze > requirements.txt
```

# debug on localhost
```
vercel dev
```
参照 http://localhost:3000
# deploy
```
vercel
```
以下 デモページ
# demo hello
```
curl https://python-api-liart.vercel.app/api/hello
```
[click here](https://python-api-liart.vercel.app/api/hello)
# demo date
```
curl https://python-api-liart.vercel.app/api/date
```
[click here](https://python-api-liart.vercel.app/api/date)
# demo star
```
curl https://python-api-liart.vercel.app/api/star
```
[click here](https://python-api.ming-taiwan.vercel.app/api/star)
# デプロイメントのURLは、vercelを実行したときに取得されます（以下の図を参照）。
when you run "vercel" it will show your endpoint of the api server
![](https://paper-attachments.dropbox.com/s_ABC4EF72CAE6330A7110BF5598F7628D572897B760F2581D1EDFC941719A6DF4_1602345294957_Screen+Shot+2020-10-10+at+11.54.31+PM.png)

# production
```
vercel --prod
```
[click here](https://python-api-liart.vercel.app/api/star)
