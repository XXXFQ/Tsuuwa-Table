import streamlit as st
from .utils import convert_text, build_speech_component

def main(argv=None):
    """Streamlit アプリのメイン関数"""
    st.set_page_config(page_title="通話表コンバーター", page_icon="🔤", layout="centered")

    # ---------------- サイドバー: サイトと通話表の説明 ----------------
    with st.sidebar:
        st.header("ℹ️ このアプリについて")
        st.markdown(
            """
            **通話表（フォネティックコード）** は、無線や電話で聞き間違いを防ぐために、
            1 文字ずつを決まった単語で言い換えて伝える方式です。
            
            - 🇯🇵 **和文通話表**：「朝日のア」「いろはのイ」…
            - 🌐 **NATO フォネティックコード**：`Alpha`, `Bravo`, `Charlie` …
            
            当アプリは文字列を両通話表へ即時変換し、Web Speech API で読み上げまで行います。
            """
        )
        st.markdown("---")
        st.markdown(
            """
            **使い方**
            1. 入力欄に文字列を入力
            2. ラジオボタンで和文／NATO を切り替え
            3. 🔊 ボタンで読み上げを実行
            
            > 音声合成はブラウザ依存です。モバイルでは長文が途中で途切れる場合があります。
            """
        )
        st.caption("© 2025 ARM / MIT License")

    # ---------------- メインUI ----------------
    st.title("📞 通話表コンバーター")

    # ユーザーにアルファベットの選択を促す
    alphabet = st.radio("アルファベットを選択", ("和文通話表", "NATO (英語)"), horizontal=True)

    # 入力欄の表示
    text = st.text_input("変換したい文字列を入力", placeholder="例: あい123", key="input_text")

    # 入力があれば変換を実行
    if text:
        phrases = convert_text(text, alphabet)
        phrase_str = "、".join(phrases)

        st.subheader("変換結果")
        st.write(phrase_str)

        lang_code = "ja-JP" if alphabet == "和文通話表" else "en-US"
        st.components.v1.html(build_speech_component(phrase_str, lang_code), height=120)

        with st.expander("詳細 (文字ごとの対応)"):
            for original, phrase in zip(text, phrases):
                st.write(f"{original} → {phrase}")
    else:
        st.info("上の入力欄にテキストを入力してください。")

    st.markdown("---")
    st.caption("© 2025 ARM")
