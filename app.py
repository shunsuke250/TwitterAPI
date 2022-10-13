from logging import PlaceHolder
import streamlit as st
import pandas as pd

st.title('Twitter　感情分析アプリ')
st.caption('Twitter APIを利用してツイートを検索し感情分析した結果を表示します')
# st.subheader('自己紹介')
# st.text('textaaaaaa')

# code = '''
# import streamlit as st

# st.title('アプリ')
# '''

# st.code(code, language='python')


with st.form(key='tweetSearch'):
    # テキストボックス
    searchWord = st.text_input('ツイートを検索', 'コロナ')

    # セレクトボックス
    searchTweetCount = st.radio(
        '検索ツイート数',
        ('10件', '50件', '100件'))

    # ボタン
    searchButton = st.form_submit_button('検索')
    cancelButton = st.form_submit_button('キャンセル')

    if searchButton:
        st.text(f'{searchWord}に関するツイートを{searchTweetCount}検索')



# データ分析関連
df = pd.read_csv('ML-Ask-08-28-test.csv', index_col=0)
# st.dataframe(df)
st.table(df)

