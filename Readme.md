# クソリプと誹謗中傷をなくそうプロジェクト
## abstract
近年，ネットリンチが社会問題になりつつある．
2020年5月にはプロレスラーの木村花 様がTwitterによる誹謗中傷が原因で自死する事件が起きた．本稿では，このように誹謗中傷などのクソリプが原因で自殺する人や心を病んでしまう人が社会問題となりつつある中で，ネットリンチを受けている人を救う目的と，ネットリンチしている人に「ネットリンチが罪である事」を認知させるための「クソリプと誹謗中傷をなくそうプロジェクト」を提案する．

<img src="./img/example.png" width="380">

## 機能
1. AIがクソリプを送ってきたユーザーをミュートする．

    [ここ](https://41pu0ds06l.execute-api.us-east-2.amazonaws.com/default/twitter-api-callback?oauth_token=a&oauth_verifier=a)で連携アプリを承認後使えるようになる
2. AIがクソリプに対し警告する．
    
    Twitterで[@satokibi44](https://twitter.com/satokibi44)宛に「Hey!クソリプbot，クソリプに対して警告して」とリプライを送信することでユーザー登録，「Hey!クソリプbot，クソリプに対して警告しないで」とリプライを送信することでユーザー登録解除


## 作った理由
誹謗中傷などのクソリプが原因で自殺する人や心を病んでしまう人が社会問題となっている中で，そのような人たちを救いたいと思ったから．

## 工夫した点
クソリプを防ぐ様々なアプリが開発されれば，もっと社会はよくなると思ったので，クソリプ計算をAPI化した．

## 使用技術
MySQL,AWS(lambda, RDS, Cloudwatch)Docker,github actions, serverless framework
## インフラ構造
クソリプ度を測るAPIは[ここ](https://github.com/satokibi44/Kusorep_API)を参照
<img src = "./img/infra.png">
