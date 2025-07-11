import streamlit as st

from .utils import convert_text, build_speech_component

def main(argv=None):
    """
    Streamlit アプリのメイン関数
    """
    st.set_page_config(page_title="通話表変換", page_icon="🔤", layout="centered")
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
