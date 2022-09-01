## TwitterAPIの利用方法

1. TwitterAPIを利用するためにDeveloper Platformで申請  https://developer.twitter.com/en

2. twitterAPI.ipynbファイルのapi_key, api_secret, access_token, access_secretにそれぞれ申請して取得した自分のキーを入力する

3. 実行はGoogle Colaboratoryで行う https://colab.research.google.com/?hl=ja


## 各コードの概要

### twitterAPI.ipynb

このソースコードは卒業研究2021年のTweet.ipynbをベースとして利用している

Tweepyのライブラリを利用してTwitterAPIを実行している

Tweepyのバージョンは3.6.0を利用

### 変更点

1. 取得するデータの変更

    ツイートの文章だけの取得から、ユーザー名(@から始まるもの)、ツイートをした日付と時刻、位置情報(指定がない場合はNoneとなる)、ツイート文の4種類に変更
    
    Botの完全な除去は不可能だが、明らかにツイート量が多いbotアカウントの情報を取得しないように設定(APIの取得時間とデータ量の削減ができるようになった)


2. データの保存方法の変更

    取得した各データを半角スペース区切りでtxtファイルで保存していたものを、カンマ区切りのcsvファイルで保存するように変更
    
    作成されるcsvファイルの先頭行には見出しを追加した (sc_name, datetime, location, text)


3. APIの実行時間削減のための効率化

    以前はAPIの実行制限にひっかならないようにtime.sleep(3)等でスリープさせていたが、ツイート件数が多いキーワードの場合、取得できずにエラーになることがわかった
    
    そこで問題解決のために、APIの実行制限にかかった際にエラーで処理を止めないようにwait_on_rate_limit=Trueを追加
    
    また、wait_on_rate_limit_notify=Trueを追加することで制限にかかった際に通知するように設定した
    
    これによりtime.sleep(3)は必要なくなり、timeモジュールを削除した
