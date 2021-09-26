# クソリプと誹謗中傷をなくそうプロジェクト
## abstract
近年，ネットリンチが社会問題になりつつある．
2020年5月にはプロレスラーの木村花 様がTwitterによる誹謗中傷が原因で自死する事件が起きた．本稿では，このように誹謗中傷などのクソリプが原因で自殺する人や心を病んでしまう人が社会問題となりつつある中で，ネットリンチを受けている人を救う目的と，ネットリンチしている人に「ネットリンチが罪である事」を認知させるための「クソリプと誹謗中傷をなくそうプロジェクト」を提案する．

<img width="380" alt="クソリプ警告" src="https://user-images.githubusercontent.com/52820882/134812732-fa0ce121-5403-4f31-8529-850654666c89.png">

## 機能
1. AIがクソリプ(クソリプ度が60点以上のクソリプ)を送ってきたユーザーを自動ミュートする．

    [ここ](https://41pu0ds06l.execute-api.us-east-2.amazonaws.com/default/twitter-api-callback?oauth_token=a&oauth_verifier=a)で連携アプリを承認後使えるようになる．
2. AIがクソリプに対し警告する．

    Twitterで[@satokibi44](https://twitter.com/satokibi44)宛に「Hey!クソリプbot，クソリプに対して警告して」とリプライを送信することでユーザー登録，ユーザー登録をすることで俺([@satokibi44](https://twitter.com/satokibi44))がクソリプに対して警告する．
    「Hey!クソリプbot，クソリプに対して警告しないで」とリプライを送信することでユーザー登録解除できる．
    
## 作った理由
誹謗中傷などのクソリプが原因で自殺する人や心を病んでしまう人が社会問題となっている中で，そのような人たちを救いたいと思ったから．

## 工夫した点
クソリプを防ぐ様々なアプリが開発されれば，もっと社会はよくなると思ったので，クソリプ計算をAPI化した．

## シーケンス図
<img alt="シーケンス図" src="https://user-images.githubusercontent.com/52820882/134813318-4d2c9b8d-5cab-43bb-8936-9fd2ee1aed66.png">

## 使用技術
Python, MySQL,AWS(lambda, RDS, Cloudwatch, NatGateway, VPC, subnet) Twitter Auth, github actions, serverless framework
## インフラ構造
クソリプ度を測るAPIは[ここ](https://github.com/satokibi44/Kusorep_API)を参照
<img width="704" alt="クソリプ警告のインフラ" src="https://user-images.githubusercontent.com/52820882/134812949-5c0c5c9a-485d-4824-b2a3-7bf80fc07aca.png">
