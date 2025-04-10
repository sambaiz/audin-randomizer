import streamlit as st
import random
from datetime import datetime

# 1人の島のリスト
single_person_islands = [
    "スカイ島",
    "ロフォーテン",
    "マン島",
    "シェットランド諸島",
    "フェロー諸島"
]

# 表の島のリスト（裏の島とフエゴ島を除く）
front_islands = [
    "スカイ島",
    "ロフォーテン",
    "マン島",
    "シェットランド諸島",
    "フェロー諸島",
    "アイスランド",
    "グリーンランド",
    "アウター・ヘブリディーズ",
    "アイラ島"
]

# 表の島と裏の島の対応関係
island_pairs = {
    "マン島": "リムリック",
    "ロフォーテン": "オークニー",
    "スカイ島": "ウェックスフォード",
    "シェットランド諸島": "ビュルネイ島",
    "フェロー諸島": "バフィン島",
    "アイラ島": "ウォーターフォード",
    "アウター・ヘブリディーズ": "コーク",
    "アイスランド": "ラブラドール島",
    "グリーンランド": "ニューファンドランド",
}

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
- フエゴ島は必ず含まれます
- 1人の島（スカイ島、ロフォーテン、マン島、シェットランド諸島、フェロー諸島）が少なくとも1つ含まれます
- 裏の島は選ばれませんが、対応する裏の島がある場合は表示されます
- 同じ日付であれば、同じ結果が表示されます
""")

# 現在の日付を取得
current_date = datetime.now().strftime("%Y-%m-%d")

# 日付をシード値として使用
random.seed(current_date)

# 1人の島を1つランダムに選択
selected_single_island = random.choice(single_person_islands)

# 残りの表の島から5つを選択（1人の島を除く）
remaining_front_islands = [island for island in front_islands if island != selected_single_island]
if len(remaining_front_islands) < 5:
    st.error("表の島の数が不足しています。")
    st.stop()
selected_remaining_islands = random.sample(remaining_front_islands, 5)

# 結果を組み合わせる（合計8つになるように）
selected_islands = selected_remaining_islands + [selected_single_island, "フエゴ島"]

# 結果を表示
st.markdown("### 選ばれた島:")
st.markdown(f"*{current_date}の結果*")

for i, island in enumerate(selected_islands, 1):
    if island in island_pairs:
        st.markdown(f"{i}. {island} - 裏: {island_pairs[island]}")
    else:
        st.markdown(f"{i}. {island}")

# フッター
st.markdown("---")
st.markdown("© 2024 オーディンの祝祭の島 ランダマイザ")