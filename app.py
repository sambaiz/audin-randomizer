import streamlit as st
import random

# 島のリスト
islands = [
    "スカイ島",
    "ロフォーテン",
    "マン島",
    "シェットランド諸島",
    "フェロー諸島",
    "リムリック",
    "オークニー",
    "アイスランド",
    "グリーンランド",
    "アウター・ヘブリディーズ",
    "アイラ島",
    "ビュルネイ島",
    "ウェックスフォード",
    "フエゴ島",
    "ケイスネス",
    "バフィン島"
]

# ページ設定
st.set_page_config(
    page_title="オーディンの祝祭の島 ランダマイザ",
    page_icon="🏝️",
    layout="centered"
)

# タイトル
st.title("🏝️ オーディンの祝祭の島 ランダマイザ")
st.markdown("---")

# 説明文
st.markdown("""
このアプリは、オーディンの祝祭の島から8つの島をランダムに選びます。
フエゴ島は必ず含まれます。
""")

# ランダマイズボタン
if st.button("島をランダマイズ", type="primary"):
    # フエゴ島を除いた島のリストを作成
    islands_without_fuego = [island for island in islands if island != "フエゴ島"]
    
    # 7つの島をランダムに選択
    selected_islands = random.sample(islands_without_fuego, 7)
    
    # フエゴ島を追加
    selected_islands.append("フエゴ島")
    
    # 結果を表示
    st.markdown("### 選ばれた島:")
    for i, island in enumerate(selected_islands, 1):
        st.markdown(f"{i}. {island}")