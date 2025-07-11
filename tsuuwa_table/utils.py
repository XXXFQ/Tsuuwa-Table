from .mappings import JP_MAPPING, EN_MAPPING

def kana_to_hiragana(ch: str) -> str:
    """
    カタカナをひらがなに変換 (該当しないものはそのまま返す)
    """
    code = ord(ch)
    if 0x30A1 <= code <= 0x30F4:  # Katakana range
        return chr(code - 0x60)
    return ch

def convert_text(text: str, alphabet: str) -> list[str]:
    """
    文字列を通話表に変換し、フレーズのリストを返す
    """
    if alphabet == "和文通話表":
        phrases = []
        for ch in text:
            hira = kana_to_hiragana(ch)
            phrases.append(JP_MAPPING.get(hira, ch))
        return phrases
    else:
        phrases = []
        for ch in text.upper():
            phrases.append(EN_MAPPING.get(ch, ch))
        return phrases

def build_speech_component(phrase_str: str, lang: str) -> str:
    """
    Web Speech API を呼び出す JS/HTML スニペットを生成
    """
    escaped = phrase_str.replace('"', '\\"')
    return f"""
    <button onclick=\"speak()\">🔊 読み上げ</button>
    <script>
    function speak() {{
      const utter = new SpeechSynthesisUtterance(\"{escaped}\");
      utter.lang = \"{lang}\";
      speechSynthesis.speak(utter);
    }}
    </script>
    """
